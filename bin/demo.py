#! /usr/bin/env python

from sparse_recon.sparse_deconv import sparse_deconv
import tifffile as tf
import numpy as np
import fire
import pathlib

from ome_zarr.reader import Reader
from ome_zarr.io import parse_url
from ome_zarr.writer import write_image
import zarr


def load_ome_zarr_img(img_p):
    reader = Reader(parse_url(img_p))
    nodes = list(reader())
    return nodes[0].data

def main(img_p, stem, pixelsize=65, resolution=280):
    img = load_ome_zarr_img(img_p + "/0/")[0][:, 1, :].squeeze()
    print(img)
    processed = img.map_overlap(sparse_deconv, \
                sigma=resolution / pixelsize, \
                background=0, \
                depth=(30, 30), dtype = np.uint32
            )
    path = pathlib.Path(f"{stem}.zarr")
    store = parse_url(path, mode="w").store
    root = zarr.group(store=store)
    group = root.create_group("deconvolved")
    write_image(processed.compute(), group, axes="yx")


if __name__ == '__main__':
    fire.Fire(main)

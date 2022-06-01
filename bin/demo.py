#! /usr/bin/env python

from sparse_recon.sparse_deconv import sparse_deconv
from dask_image.imread import imread
import tifffile as tf
import numpy as np
import fire


def main(img_p, stem, pixelsize=65, resolution=280):
    img = imread(img_p)#[1, 10000:13000, 10000:13000]
    img = img.rechunk([1, 3000, 3000])
    img = img[5]
    print(img)
    processed = img.map_overlap(sparse_deconv, \
                sigma=resolution / pixelsize, \
                background=0, \
                depth=(30, 30), dtype = np.uint32
            )
    tf.imwrite(f"{stem}_processed.tif", processed)

if __name__ == '__main__':
    fire.Fire(main)

#!/usr/bin/env/ nextflow
// Copyright © 2022 Tong LI <tongli.bioinfo@protonmail.com>

nextflow.enable.dsl=2

params.img = ""
params.ourdir = "./output/"

params.pixelsize = 65
params.resolution = 280

params.docker_image = "sparse_deconv"

process deconv {

    container params.docker_image
    containerOptions "--gpus all"
    publishDir params.ourdir, mode :"copy"

    input:
    path img
    val pixelsize
    val resolution

    output:
    path "${stem}_processed.tif"

    script:
    stem = img.baseName
    """
    demo.py --img_p ${img} --stem ${stem} \
        --pixelsize ${pixelsize} --resolution ${resolution}
    """
}


workflow {
    deconv(params.img, params.pixelsize, params.resolution)
}

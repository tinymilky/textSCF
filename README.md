# TextSCF: LLM-Enhanced Image Registration Model

![Pytorch](https://img.shields.io/badge/Implemented%20in-Pytorch-red.svg) <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a> [![arXiv](https://img.shields.io/badge/arXiv-2111.10480-b31b1b.svg)](https://arxiv.org/abs/2311.15607)

TextSCF is a comprehensive library designed for weakly supervised image alignment and registration, providing extensive utilities for detailed deformation field analysis.

## Updates

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="20"> [12/06/2023] - The code for textSCF, reproducing our results for task 3 in [MICCAI 2021 Learn2Reg Challenge](https://learn2reg.grand-challenge.org/evaluation/task-3-validation/leaderboard/), is now available. See datasets and usage sections below.

<img src="https://user-images.githubusercontent.com/74038190/216122069-5b8169d7-1d8e-4a13-b245-a8e4176c99f8.png" width="18"> [11/30/2023] - We collect a list of papers exploring the use of LLMs in AI for medicine and healthcare. ([Awesome-Medical-LLMs](docs/Awesome-Medical-LLMs.md)) <br>
<img src="https://user-images.githubusercontent.com/74038190/216122069-5b8169d7-1d8e-4a13-b245-a8e4176c99f8.png" width="18"> [11/30/2023] - We collect a list of papers centered on image registration models in healthcare. ([Awesome-Medical-Image-Registration](docs/Awesome-Medical-Image-Registration.md))

## Papers

**[Spatially Covariant Image Registration with Text Prompts](https://arxiv.org/abs/2311.15607)** <br>
[Hang Zhang](https://tinymilky.com), [Xiang Chen](https://grzy.hnu.edu.cn/site/index/chenxiang), Rongguang Wang, Renjiu Hu, [Dongdong Liu](https://ddliu365.github.io/), and [Gaolei Li](https://icst.sjtu.edu.cn/DirectoryDetail.aspx?id=28). <br>
arXiv 2023.

**[Spatially Covariant Lesion Segmentation](https://www.ijcai.org/proceedings/2023/0190)**  <br>
[Hang Zhang](https://tinymilky.com), Rongguang Wang, Jinwei Zhang, [Dongdong Liu](https://ddliu365.github.io/), Chao Li, and Jiahao Li.  <br>
IJCAI 2023.

## Highlights

- The textSCF (random_cat) ranks **1st** on the validation set of task 3 in [MICCAI 2021 Learn2Reg Challenge](https://learn2reg.grand-challenge.org/evaluation/task-3-validation/leaderboard/).
<p align="center">
    <img src="https://github.com/tinymilky/TextSCF/blob/main/figs/OASIS_L2R_2021_task03_leaderboard_screenshot.png" width="600"/>
</p>

- The deformation field generated by textSCF effectively demonstrates its ability to preserve discontinuities across different anatomical regions. As illustrated in the image below, it outlines the stomach in contrast to the adjacent regions.
<p align="center">
    <img src="https://github.com/tinymilky/TextSCF/blob/main/figs/discontinuity_preserving.png" width="600"/>
</p>

- TextSCF is designed to integrate with various architextures, including [LKU-Net](https://github.com/xi-jia/LKU-Net), [LapRIN](https://github.com/cwmok/LapIRN), [VoxelMorph](https://github.com/voxelmorph/voxelmorph), and [TransMorph](https://github.com/junyuchen245/TransMorph_Transformer_for_Medical_Image_Registration), showcasing its utility in medical image registration.
<p align="center">
    <img src="https://github.com/tinymilky/TextSCF/blob/main/figs/dice_bar.png" width="600"/>
</p>

## Datasets

See [Datasets](docs/Datasets.md) for more details.

## Usage
Run the script with the following command to reproduce the results:
```
python train_brainreg.py -d oasis_pkl -m brainTextSCFComplex -bs 1 --epochs 501 --reg_w 0.1 start_channel=64 scp_dim=2048 diff_int=0 clip_backbone=vit
```

- `-d oasis_pkl`: Dataset used, specifically 'oasis_pkl'.
- `-m brainTextSCFComplex`: Model name, set to 'brainTextSCFComplex'.
- `-bs 1`: Batch size, defined as 1.
- `--epochs 501`: Total number of epochs for training, set to 501.
- `--reg_w 0.1`: Smoothness regularization weight, specified as 0.1.
- `start_channel=64`: Number of starting channels (`N_s`), set to 64.
- `scp_dim=2048`: The dimension (`C_{\phi}`) for the implicit function, set to 2048.
- `diff_int=0`: Diffeomorphic integration flag, '0' for not used.
- `clip_backbone=vit`: [CLIP](https://github.com/openai/CLIP) backbone type, specified as 'vit' (ViT-L/14@336px).

Please note that using a starting channel of 64 is computationally intensive. It is recommended to run this on an A100 GPU or higher for optimal performance. Alternatively, you can reduce the starting channel to as low as 8 for increased efficiency, while still achieving a Dice score of approximately 87.

## Todo
- [x] Awesome-Medical-LLMs
- [x] Awesome-Medical-Image-Registration
- [x] Core code release
- [ ] Pretrained model release
- [ ] Support of different backbones and datasets
- [ ] Tutorials and periphery code
    - [ ] Smoothness and complexity analysis
    - [ ] Statistical analysis
    - [ ] Discontinuity-preserving deformation field

## Citation
If our work has influenced or contributed to your research, please kindly acknowledge it by citing:
```
@misc{zhang2023spatially,
      title={Spatially Covariant Image Registration with Text Prompts}, 
      author={Hang Zhang and Xiang Chen and Rongguang Wang and Renjiu Hu and Dongdong Liu and Gaolei Li},
      year={2023},
      eprint={2311.15607},
      archivePrefix={arXiv},
      primaryClass={eess.IV}
}

@inproceedings{ijcai2023p0190,
  title     = {Spatially Covariant Lesion Segmentation},
  author    = {Zhang, Hang and Wang, Rongguang and Zhang, Jinwei and Liu, Dongdong and Li, Chao and Li, Jiahao},
  booktitle = {Proceedings of the Thirty-Second International Joint Conference on
               Artificial Intelligence, {IJCAI-23}},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},
  editor    = {Edith Elkind},
  pages     = {1713--1721},
  year      = {2023},
  month     = {8},
  note      = {Main Track},
  doi       = {10.24963/ijcai.2023/190},
  url       = {https://doi.org/10.24963/ijcai.2023/190},
}

```
## Acknowledgment

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/03H_UnPI)
# Title (Please modify the title)
## Team

| ![박패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![이패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![최패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![김패캠](https://avatars.githubusercontent.com/u/156163982?v=4) |
| :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: |
|            [이강건](https://github.com/Uncommonness)             |            [한지승](https://github.com/wltmd1114)             |            [홍재민](https://github.com/HongJaeMin)             |            [이승현](https://github.com/EffortLEE1008)             |
|                            팀장, <br> EDA, <br> kobart, <br> T5-small/base/large, <br> Data Preprocessing                            |                            팀원, <br> 발표, <br> kobart, <br> baseline experiment                            |                            팀원, <br> EDA, <br> kobart, <br> T5-small/base/large, <br> Data Preprocessing, <br> Notion template                            |                            팀원, <br> kobart, <br> baseline experiment, <br> Rouge score                             |

## 0. Overview
### Environment
- Python
- Pytorch
- transformers

### Requirements
- torch
- pandas
- rouge
- yaml
- transformers
- wandb

## 1. Competiton Info

### Overview

- Deep Learning Model을 이용하여 Dialogue Summarization을 진행한다.

### Timeline

- May 13, 2024 - Start Date
- May 27, 2024 - Final submission deadline

## 2. Components

### Directory

- HJM
- HJS
- LKK
- LSH

## 3. Data descrption

### Dataset overview

- train: (12457, 4)
- dev: (499, 4)
- test: (499, 2)

### EDA

- LKK/EDA/EDA.ipynb
- HJM/DB/basic-preprocessing/token_check.ipynb

### Data Processing

- Data Cleaning
    - LKK/Preprcessing/Preprocessing.ipynb
    - HJM/DB

## 4. Modeling

### Model

Hugging Face

- bart
    - digit82/kobart-summarization
    - ainize/kobart-news
    - EbanLee/kobart-summary-v3
    - alaggung/bart-r3f
    - gogamza/kobart-summarization
- t5
    - lcw99/t5-base-korean-text-summary
    - lcw99/t5-large-korean-text-summary
    - eenzeenee/t5-base-korean-summarization
    - paust/pko-t5-large

### Modeling Process

- Hugging Face Model Load 후, 최적의 Config 조합 찾기 위해, 실험

## 5. Result

### Leader Board

### Public 43.4391 (5th)
![image](https://github.com/UpstageAILab2/upstage-nlp-summarization-nlp-06/assets/107130478/95148e17-888f-473b-8b49-6b23bf6fa0b1)

### Private 0.9336 (5th)
![image](https://github.com/UpstageAILab2/upstage-cv-classification-cv-06/assets/107130478/c30427f3-d94d-4dee-be89-05af07189837)

### Presentation

- [패스트캠퍼스]-Upstage-AI-Lab-3기-6조-CV경진대회.pdf

## etc

### Meeting

- Slack, Zoom, Notion

### Reference

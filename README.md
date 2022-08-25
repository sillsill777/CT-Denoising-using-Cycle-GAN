# Low Dose CT Denoising using Cycle GAN
### Using Low Dose CT data from [AAPM](https://www.aapm.org/)

You can find details about Low Dose CT Grand Challenge from this [Official Website.](https://www.aapm.org/grandchallenge/lowdosect/#trainingData)

You can download data set(~8.3GB) from [data link](https://drive.google.com/drive/folders/1pC7Coiu3bcPAy2Kno7b6jdyLzcs-G1Gz?usp=sharing).

Download the data and place ```data``` folder in main project directory.

- - -

## Objective
- The goal of this challenge and our project is to denoise low dose(quarter dose) CT Image to get high dose(full dose) CT Image.

## Data Preview
Inside the ```data``` folder you will find two sub folder ```qd``` and ```fd``` each representing quarter dose and full dose.

Quarter dose corresponds to low dose and full dose corresponds to high dose.

Typical data look like below.

<img src="./images_README/full_image.png">

You can see the noise in quarter dose image compared to full dose image. 

For clarity, I also included center cropped image below.

<img src="./images_README/crop_image.png">

## Model Structure

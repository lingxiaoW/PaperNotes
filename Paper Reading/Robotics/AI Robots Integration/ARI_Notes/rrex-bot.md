- **RREx-BoT Remote Referring Expressions with a Bag of Tricks**
 **[`arXiv 2023`]** *Gunnar A. Sigurdsson, Jesse Thomason, Gaurav S. Sukhatme, Robinson Piramuthu* [(arXiv)](http://arxiv.org/abs/2301.12614) [(pdf)](./RREx-BoT%20Remote%20Referring%20Expressions%20with%20a%20Bag%20of%20Tricks.pdf) (Citation: 0)
    <p align="center">
    <img src="./../../images/remote_referring.png" width="60%">
    </p>

  - Using a generic vision-language scoring model with minor modifications for 3D encoding and operating in an embodied environment. 
  - Two challenges when applying an off-the-shelf, generic vision-and-language alignment scoring model to the task of remote, embodied visual referring expression resolution. 
    - Such VL models are trained only on 2d images
    - These models output match scores between image proposals and target language in batches, but we cannot fit hundreds of thousands of object proposal regions in a single batch, making ranking language-image match scores between batches non-trivial. 
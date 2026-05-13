# CutSharp: A Simple Data Augmentation Method for Learned Image Compression

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Learned image compression (LIC) methods have demonstrated superior rate$-$distortion performance, compared to traditional ones. Previous studies on LIC have mainly focused on models, consisting of analysis/synthesis transformations and entropy models. Unfortunately, the importance of $data$ has usually been neglected when training LIC models. In this paper, we introduce block-wise RGB standard deviation as a measure for estimating the compression-related difficulty of images. Next, we emphasize the significance of effective data utilization for LIC by demonstrating that models trained on a certain subset of data, constructed according to the block-wise RGB standard deviation, can achieve superior rate$-$distortion performance to models trained on the entire data. Inspired by this observation, we propose a simple data augmentation technique for LIC, coined CutSharp, which enhances image sharpness within an arbitrary region. Our proposed augmentation consistently improves rate$-$distortion performance on the Kodak and CLIC validation dataset. We hope that our work will encourage further research in data-centric approaches for LIC.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a simple data augmentation method, called Cutsharp, for learned image compresion problem. Specifically, the authors first introduce block-wise RGB standard deviation as a measure for estimating the compression difficulty of images. Then they demonstrate that compression models trained on a certain subset of images, selected from the entire training set according to the block-wise RGB standard deviation, can achieve superior rate-distortion performance to the models trained on the entire dataset. Inspired by the above observation, the authors propose a data augmentation strategy to boost the peformance of the neural image compression model, called Cutsharp, which enhances image sharpness within an randomly selected region in the training images.

### Strengths
- This paper seeks to investigate a new question: how the quality of the training data affects the results of rate-distortion optimization, which has been neglected in previous studies.
- The experiments are comprehensive and some of the findings are very interesting, e.g,. there is a strong correlation between the block-wise RGB standard deviation and the compression difficulty.
- The idea of dividing training images into different groups according to the B-RGB-SD metric is great.

### Weaknesses
 - The finding  "_models trained on a subset of dataset, based on B-RGB-SD can outperform models trained on the entire dataset_" is meaningless. It is just some kind of __overfitting__. 
The test dataset, either Kodak or CLIC, only contain a few dozen images.
When dividing the entire dataset into different groups according to the B-RGB-SD metric, one of the divided subsets happens to be closer to the test set in some of the statistical properties  (e.g, B-RGB-SD). So It is no doubt that the model trained on this subset will lead to a better result on the test set. I think that Figure 4 can only prove that the subset of top 20-40% B-RGB-SD is closer to Kodak than other subsets and the subset of top 60-80% B-RGB-SD is the one closest to CLIC dataset.

- Another major weakness of this paper is lack of motivation. Only the data augmentation method (Cutsharp) is given, but there is no explanation as to why it is designed this way. Why sharpening and why cut?  
 -- Why sharpening? There are so many operations for low-level image processing, why choose sharpening?  What is the specificity of the sharpening operation? Why not try the combination of different operations?  
 -- Why cut? What will happen if the operation (such as sharpening) performed on the entire image?

### Questions
Please see weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the problem of data augmentation for learned image compression and develops a data-centric method for this problem based on the block-wise RGB standard deviation, called CutSharp. The method aims to balance B-RGB-SD by enhancing image sharpness in the training phase. Based on CutSharp, the learned image compression achieves better rate-distortion performance. The paper presents superior results across various learned image compression methods on the Kodak and CLIC datasets.

### Strengths
1. CutSharp is a simple and direct data-centric approach that utilizes data effectively in learned image compression.

2. CutSharp leads to consistent rate–distortion performance improvement across diverse learned image compression.

### Weaknesses
1. My major concern is the limited technical novelty and contribution of the paper. CutSharp is a simple idea but just a variant of the sharpening method -- sharpen the random region of an image. It compensates for the imbalance of B-RGB-SD of the cropped image.

2. The experiments in the paper are not convincing and the overall performance of CutSharp is not strong enough. First of all, the improvement of CutSharp on Kodak (-0.39%) and CLIC (-0.40%) is worse than Sharpening=0.50 on Kodak (-0.46%) and ColorJitter=0.2 on CLIC (-0.63%).  The visualization of learned motion patterns in Fig. 5 seems not appealing enough.

3. The analysis of B-RGB-SD is not convincing enough. The experiments reveal that B-RGB-SD is more effective in capturing the compression-related difficulty of an image. However, it is not clear how B-RGB-SD influences the compression performance.

### Questions
1. Sec.5.2 said "In other words, during training, the original image is cropped to a smaller size, which is more likely to have a low B-RGB-SD because typically only a small portion of the original image has high B-RGB-SD." -> How did you come to this conclusion? More experiments are suggested to support this claim. 
  
2. If the claim of Q1 is true, the problem of imbalance on B-RGB-SD may come from the crop process during training. The crop process leads to low B-RGB-SD samples. I am wondering what if you drop the low B-RGB-SD samples?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses three things
1) How to measure "difficulty" of an image
2) Use the above measure to train on a subset of the data according to its difficulty
3) Use an augmentation called CutMix

### Strengths
It is interesting that CutSharp improves BD-Rate marginally.

### Weaknesses
Part 1: Difficulty of an image. Authors propose using RGB standard deviation of RGB blocks to get a measure for the difficulty of an image, and show in Fig 2. how this correlates to bpp/PSNR. They report a person correlation. The weakness lies in no baselines given: if we have a codec (eg even just JPEG) we can trivially calculate bpp/PSNR and with two or more images we could fit a line. How does that compare to the proposed method?

Part 2: Table 1 does not show an actionable insight. The proposed B-RBG-SD is apparently not enough to select a subset, because the optimal subset is only known after trainign a model on each. I.e. The authors cannot come up with a prediction of what a useful subset is, so the method is meaningless. In Fig.4, we also don't see a novel insight: training on hard examples improves hard inference, but makes easy images worse, and vice-versa, this is just classical ML: you are good where you train.

Part 3: CutSharp: The augmentation provides very miniuscule gains only (Table 4) and in Fig 5 we see no obvious visual diff (not surprising given the tiny PSNR diffs, e.g., 0.05dB between a) and d).

Overall, this paper does not contain insights or results that warrant an ICLR publication.

### Questions
Generally, people use augmentation because labelling is hard. In image compression, one can just get more data, no labels required. It would have been insightful to double the training set and see how that affects BD-rate gains. I'd be surprised if CutSharp gets bigger gains than you get from doubling the dataset.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
## Summary
This paper study the data aspect of learned image compression. An interesting analysis using different subset of dataset shows that the performance of learned image compression is effected by the difficulty of images. Motivated by this, the authors propose a novel data augumentation approach for image compression, which brings an improvement of BD-BR of 0.66\%.

### Strengths
## Strength
* This paper discusses an unexplored area of learned image compression.
* The method proposed by this paper is well motivated and the analysis using different subsets of dataset is convincing.
* This paper is well-written and clearly presented.

### Weaknesses
## Weakness
* First of all, the necessity of data augmentation for image compression, especially for natural images, is questionable. While the authors propose using a subset of Openimage (300k), larger datasets like LAION-5b (5,000,000k) are readily available and haven't been fully utilized in this domain. The authors' claim that training on 300k images for 90 epochs necessitates 27,000k unique images is technically correct, but it overlooks the fact that datasets like LAION-400M (400,000k) or LAION-5B high res (170,000k) vastly exceed this requirement. Directly leveraging these larger datasets seems a more straightforward approach than augmenting a smaller one, given the abundance of natural image data.
* Second, the empirical results presented, particularly the BD-BR improvement of -0.66%, are not compelling enough to justify the proposed data augmentation technique. A -0.66% BD-BR improvement, especially without reported standard deviations, lacks the statistical significance to support the claims of the paper. To put this into perspective, a -5.0% BD-BR improvement roughly translates to a 0.2 dB improvement in BD-PSNR. The reported improvement is marginal and does not demonstrate a substantial advantage over existing methods or simply using a larger dataset.

### Questions
## Questions
* It would be much more convincing if the authors are dealing with special images that are hard to acquire. For example, medical image, remote sensing image. Currently the authors only test their methods on natural image, which is too cheap to acquire and eliminates the need for data augumentation.
* The current empirical results is too weak, and the authors should provide an improvement of 2\% to 5\% improvement of BD-BR to support a paper, this might be achieved by chaning the domain of image.
* A perhaps more intuitative measure of difficulty is the distance between single image's R-D and average R-D curve. This can be obtained by any pre-trained image codec. It would be interesting to see whether this achieves the same effect as B-RGB-SD.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

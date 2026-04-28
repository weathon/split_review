# Halton Scheduler for Masked  Generative Image Transformer

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Masked Generative Image Transformers (MaskGIT) have emerged as a scalable and efficient image generation framework, able to deliver high-quality visuals with low inference costs. However, MaskGIT's token unmasking scheduler, an essential component of the framework, has not received the attention it deserves. We analyze the sampling objective in MaskGIT, based on the mutual information between tokens, and elucidate its shortcomings. We then propose a new sampling strategy based on our Halton scheduler instead of the original Confidence scheduler. More precisely, our method selects the token's position according to a quasi-random, low-discrepancy Halton sequence. Intuitively, that method spreads the tokens spatially, progressively covering the image uniformly at each step. Our analysis shows that it allows reducing non-recoverable sampling errors, leading to simpler hyper-parameter tuning and better quality images. Our scheduler does not require retraining or noise injection and may serve as a simple drop-in replacement for the original sampling strategy. Evaluation of both class-to-image synthesis on ImageNet and text-to-image generation on the COCO dataset demonstrates that the Halton scheduler outperforms the Confidence scheduler quantitatively by reducing the FID and qualitatively by generating more diverse and more detailed images. Our code is publicly available on [link redacted].

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new schedule for token decoding in masked image modeling. MaskGIT decodes high confidence tokens first. Instead, this paper shows that this technique is not optimal and can lead to decreased performance with more decoding steps which should not occur with a good schedule. To combat this, the paper proposes a Halton schedule based on mutual information analysis to spread out the predicted tokens. The technique requires no training and can be plugged into other models. Experiments are conducted on class conditional and text conditional image generation.

### Strengths
This paper addresses an overlooked problem: choosing which tokens to decode during masked image modeling. The intermediate analysis and motivation are clear, and the proposed solution is promising while being simple. Comparison against random decoding is also conducted.

### Weaknesses
- The paper is poorly written. There are tons of typos and layout issues making it hard to follow.
- The contribution is not enough. It is like a simple spatial prior to the sampling process.
- The experiments are limited and unfair. For example, in table 1, the author compared the proposed method with the baseline MaskGIT. However, the "Ours" baseline is not presented. The compared MaskGIT has a different # param compared to the proposed approach.
- Fig 5 is very confusing. It is not understandable. Why is only the FID/IS reported for AR mode? 
- In table 2, the results are not fair. As compared MaskGIT* is not trained to predict images in 32 steps.
- The qualitative results are also limited. What are the text prompts for fig 8?
- Fig 7 is very confusing. Is the training target of the confidence scheduler set to be 32 during training?

### Questions
NA

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the Halton Scheduler, which refines the token unmasking strategy in MaskGIT. The authors begin by analyzing the Confidence Scheduler previously designed for MaskGIT (Chang et al., 2022; 2023), which prioritizes the unmasking of the most certain tokens. They demonstrate that while this method enhances confidence, it can reduce diversity and image quality due to the clustering of tokens around already predicted regions. To address this, they propose a novel, deterministic scheduler that leverages the Halton low-discrepancy sequence (Halton, 1964). This approach is informed by understanding entropy progression during image generation, aiming for a more even distribution of token selection to ensure uniform coverage across the image. They show convincing results over baselines like MUSE and MaskGIT across image generation and text to image generation.

### Strengths
1) Overall the idea of Halton scheduler makes a lot of sense and addresses the important problem of scheduler in MaskGIT kind of models.
2) Halton scheduler proposes a improved schedule which makes the model improved generation capabilities.
3) Experimental results show pretty convincing improvements across text-to-image zero-shot COCO, MUSE , MaskGIT and other competetive methods.

### Weaknesses
Weakness:
1) How was the discretization of the sequence Hnh into a grid corresponding to the token map done? This seems to be an approximation which I’m not sure about.
2) More intuition and details need to be added especially for Halton scheduler, like the Low-Discrepancy properties need to be discussed more. 
3) Discussion on improved halton sequencing needs to be added. Using the Scrambled Halton Sequence, the Leapfrog Method, and Higher-Dimensional Generalizations need to be discussed. 
4) Similar ideas for information overload into tokens have been studied in the registers[1]. Analysis on token norm in this setting will be useful and could reflect whether there is similarity in understanding between high-norm tokens and the proposed scheduler. 
5) Is Extra compute time required to use Halton scheduler? One of the main advantages of the Halton scheduler is the speed of image generation. Would like to see what is the inference time with Halton's scheduler?
References
1) Vision Transformer needs registers.

### Questions
I don't have a good sense of what is the extra information that is being learnt using Halton schduler and the intuition is not very clear. I agree with the analysis of the paper but the proposed solution doesn't;t seem very well analysed and ablated.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel scheduler based on the Halton sequence, aimed at minimizing the correlation between simultaneously sampled tokens and maximizing the information gained at each step. By selecting token positions using a quasi-random, low-discrepancy Halton sequence, the approach reduces FID scores and improves both image quality and diversity.

### Strengths
- Presents an innovative mutual information analysis that clarifies the scheduler’s role in MaskGIT.
- By leveraging the Halton sequence, the method ensures a more even distribution of selected tokens, grounded in the information gained at each step and the mutual information between tokens.
- Enhances both image quality and diversity in class-to-image and text-to-image generation.

### Weaknesses
- The assumption for Eq. 5.b is not sufficient, which ignores the long-distance dependencies.
- The influence of conditional entropy is not limited to spatial proximity; semantic information and context play a significant role and should be considered.

### Questions
- After vector quantization, do token relationships still correspond to their Euclidean distance?
- Might this uniformity lead to the overlooking of critical details in specific areas, thus negatively impacting sampling accuracy?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposed a new sampling strategy using the Halton scheduler which uniformly recovers the image spatially. Several experiments are conducted to validate the effectiveness.

**Additional Comments**:

The manuscript does not follow the margin of ICLR template, which violates the submission guidelines. 

In all, I lean towards desk rej.

### Strengths
NA

### Weaknesses
- The paper is poorly written. There are tons of typos and layout issues making it hard to follow.
- The contribution is not enough. It is like a simple spatial prior to the sampling process.
- The experiments are limited and unfair. For example, in table 1, the author compared the proposed method with the baseline MaskGIT. However, the "Ours" baseline is not presented. The compared MaskGIT has a different # param compared to the proposed approach.
- Fig 5 is very confusing. It is not understandable. Why is only the FID/IS reported for AR mode? 
- In table 2, the results are not fair. As compared MaskGIT* is not trained to predict images in 32 steps.
- The qualitative results are also limited. What are the text prompts for fig 8?
- Fig 7 is very confusing. Is the training target of the confidence scheduler set to be 32 during training?

### Questions
NA

### Soundness
1

### Presentation
1

### Contribution
1

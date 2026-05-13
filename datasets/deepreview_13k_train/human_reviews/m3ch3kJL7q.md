# Sentence-level Prompts Benefit Composed Image Retrieval

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Composed image retrieval (CIR) is the task of retrieving specific images by using a query that involves both a reference image and a relative caption.
Most existing CIR models adopt the late-fusion strategy to combine visual and language features. 
Besides, several approaches have also been suggested to generate a pseudo-word token from the reference image, which is further integrated into the relative caption for CIR. 
However, these pseudo-word-based prompting methods have limitations when target image encompasses complex changes on reference image, \eg, object removal and attribute modification. 
In this work, we demonstrate that learning an appropriate sentence-level prompt for the relative caption (SPRC) is sufficient for achieving effective composed image retrieval. 
Instead of relying on pseudo-word-based prompts, we propose to leverage pretrained V-L models, \eg, BLIP-2, to generate sentence-level prompts.
By concatenating the learned sentence-level prompt with the relative caption, one can readily use existing text-based image retrieval models to enhance CIR performance.
Furthermore, we introduce both image-text contrastive loss and text prompt alignment loss to enforce the learning of suitable sentence-level prompts. 
Experiments show that our proposed method performs favorably against the state-of-the-art CIR methods on the Fashion-IQ and CIRR datasets.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an novel approach for the Composed Image Retrieval (CIR) problem. The idea is to generate a sentence ("text prompt") to describe both the input image and the relative caption and it for searching the image database using standard text-to-image retrieval methods. The method is evaluated against 10+ baseline methods against two datasets ( CIRR, Fashion - IQ). The results provide significant top-k recall gains over all the baselines.

### Strengths
- The proposed method is technically sound and simple. 
- The paper is easy to follow, experiments are thorough along with ablations (such as prompt length, weight in the loss function etc). 
- Provides SOTA results against 10+ baselines on two public datasets. 
- To be open-sourced.

### Weaknesses
 - Limited novelty: A recent paper (https://arxiv.org/pdf/2310.09291.pdf) with quite similar methodology and motivations except for a nuanced difference: training-free vs learned sentence level prompts. There is a need for contextualizing these methods together, ideally under the same evaluation framework so that we understand the value of learned sentence level prompts proposed by this paper. 
- Experimental setup: CIRR dataset experiments uses a random split of the training dataset as the test set for evaluations. The results should be reported in the official (hidden) test set instead. Otherwise reported numbers are not comparable to other papers published in this area.

### Questions
Q1: Could the database image-caption pairs be enriched with the proposed sentence generation method and used for refining the search?
Q2: How easy to extend the proposed method for addressing other problem domains or modalities?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a sentence prompt generation based approach to composed image retrieval or CIR. They train their system to learn the generation of such sentence prompts for known target images (in the training set) through two innovative loss functions. Then at inference time their system essentially generates a sentence prompt that along with the original user query enables the user to retrieve the target image with greater accuracy since the sentence prompt has a much more fine-grained description of the target image.

### Strengths
1. Comprehensive literature survey and good motivation of the problem.
2. Sound approach based on innovative loss functions.
3. Good results that exceed the state of the art.

### Weaknesses
1. The overall innovation could be seen as modest. However, I am open to being convinced otherwise.

### Questions
1. How does your approach do across domains? Is it able to adapt to domain shifts in other words?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to learn sentence-level prompts for supervised composed image retrieval task, to handle complex changes in CIR task such as modifications involving multiple objects. The sentence-level prompts are generated from query image and relative caption, to yield precise descriptions of specific elements in the query image that are described in the relative caption. Experimental results demonstrate that the proposed method achieves better results on two public CIR benchmarks including FashionIQ and CIRR.

### Strengths
1. It is reasonable to generate sentence-level prompts depending on both reference image and relative caption to enrich the expressivity. 
2. Moreover, the experiments are solid since the authors conduct a thorough comparison with previous methods. 
3. The paper is well-written and the idea is easy to follow.

### Weaknesses
1.  in my comprehension, the sentence-level prompts are actually latent vectors output from the MLP layer, so it is hard to make sure the prompts work as expected as demonstrated in Figure 1(c), i.e., decoupling the multiple objects and attributes of query image, and correctly integrating the process of object removal or attribute modification. 
2.  It is difficult to understand the pi’ in prompt alignment loss. Whether each reference image has an auxiliary text prompt? As a result, the Figure 2(a) involves two training stages (ITC loss to optimize p and prompt alignment loss to optimize pi’)? Furthermore, during the optimization of pi’, the text encoder is frozen, so the image encoder learns to align with the frozen text encoder; while in optimization of pi, the text encoder is not frozen, so the image encoder learns to align with the updated text encoder. I find it hard to understand how the prompt alignment loss works and it seems very tricky to achieve a good performance.

### Questions
The same as weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

# MemBench: Memorized Image Trigger Prompt Dataset for Diffusion Models

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Diffusion models have achieved remarkable success in Text-to-Image generation tasks, leading to the development of many commercial models. However, recent studies have reported that diffusion models often generate replicated images in train data when triggered by specific prompts, potentially raising social issues ranging from copyright to privacy concerns. 
To sidestep the memorization, there have been recent studies for developing memorization mitigation methods for diffusion models. 
Nevertheless, the lack of benchmarks impedes the assessment of the true effectiveness of these methods. 
In this work, we present MemBench, the first benchmark for evaluating image memorization mitigation methods. Our benchmark includes a large number of memorized image trigger prompts in various Text-to-Image diffusion models. Furthermore, in contrast to the prior work evaluating mitigation performance only on trigger prompts, we present metrics evaluating on both trigger prompts and general prompts, so that we can see whether mitigation methods address the memorization issue while maintaining performance for general prompts. This is an important development considering the practical applications which previous works have overlooked. 
Through evaluation on MemBench, we verify that the performance of existing image memorization mitigation methods is still insufficient for application to diffusion models

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a benchmark to evaluate memorization mitigation methods in text-to-image diffusion models. MemBench includes a large set of trigger prompts that replicate training images, potentially causing privacy or copyright issues. It assesses mitigation methods by examining their effectiveness in preventing memorized images without degrading general prompt performance.

### Strengths
1. The paper reformulates the search for memorized image prompts as an optimization problem, which allows for more efficient prompt discovery.
2. It employs a Markov Chain Monte Carlo (MCMC) method to solve the optimization problem, resulting in a significantly larger set of memorized prompts compared to previous methods.
3. MemBench provides evaluation of existing memorization mitigation methods in diffusion models.

### Weaknesses
1. This paper does not consider the detection problem. Wen et al and Ren et al both use detection before mitigation. So they do not always mitigate on general prompts. It does not make sense to compare the generation performance on general prompts.

2. The evaluation metrics are not new. In existing paper like Wen et al and Ren et al, they use all the metrics mentioned in this paper.

3. The dataset construction requires white-box access, which is ineffective to API-based models. In addtion, although it does not use training set, it requires to use an API to search images on the web, which is not efficient.

4. The major problem is the benchmark, which didn't provide a reasonable perspective and new metrics.

### Questions
Besides providing a larger size of dataset, what is the contribution of the new dataset?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the memorization issue in text-to-image diffusion models, where generated images is almost or exactly the same as the training image, which leads to privacy concerns. This paper propose a new triggering prompt dataset that contains prompts that will lead to memorized generations. This paper evaluates several baseline works’ mitigation strategies on the proposed datasets and also non-triggering prompts and have concluded that existing strategies still have room for improvement as they degrade overall performance of diffusion models.

### Strengths
- This paper is good in presentation, with good clarity, well-structured, and easy to follow.
- This paper addresses an important and practical task: the reverse process of the diffusion model always invokes almost or exactly the same memorized images from training data. This can lead to privacy issues, which are well-discussed and motivated in the introduction section.
- This paper proposes 3,000, 1,500, 309, and 1,352 memorized image trigger prompts for different generative models, compared to a previous benchmark that provides 325, 210, 162, and 354 prompts. Adding additional trigger prompts as a dataset is beneficial for a more comprehensive evaluation of mitigation strategies.

### Weaknesses
1. **Limited contribution**. 
- While the additional trigger prompts introduced in this paper can indeed aid in evaluating existing mitigation strategies and provide further assessment of their performance, such contribution remains somewhat incremental. Rather than addressing a critical need in the field, it adds to existing resources that are already robust. For example, prior methods [1, 2] have utilized 500 trigger prompts, which a recent work [3] systematically organized by extracting and categorizing them into three types (Matching Verbatims, Retrieval Verbatims, and Template Verbatims) based on their distinct characteristics. This categorization already offers a comprehensive framework, making the additional prompts in the present work more of an enhancement than a necessary innovation. I understand that this work’s main contribution is proposing a new benchmark trigger prompt dataset; unlike others that focus on proposing strategies to detect and mitigate the memorization problem, such core contribution (the proposed prompt dataset) is still of quite limited contribution.
- I have also carefully read all the claimed contributions in the paper and appreciate the authors’ effort in presenting them in a well-structured way that is easy to follow. However, such concern remains as the other claimed contributions are also trivial. For example, the idea of using general (non-memorized) prompts in addition to those trigger prompts for evaluation is a good point. However, it is more of a good practice for the related work, instead of a significant contribution. Also, the finding of all mitigation methods can result in a reduction of text alignment, reflecting the trade-off nature of all mitigation strategies, which is already well-documented in the related works and is not a new finding.

[1] Detecting, Explaining, and Mitigating Memorization in Diffusion Models.

[2] Unveiling and Mitigating Memorization in Text-to-image Diffusion Models through Cross Attention.

[3] A Reproducible Extraction of Training Images from Diffusion Models.

2. **Concerns regarding motivation**. I find the descriptions (motivations) in lines 46-50 to be misleading, where the paper states: “The current studies (Wen et al., 2024b; Somepalli et al., 2023b) have adopted the following workaround: 1) simulating memorization by fine-tuning T2I diffusion models for overfitting on a separate small and specific dataset of {image, prompt} pairs, and 2) assessing whether the images used in the fine-tuning are reproduced from the query prompts after applying mitigation methods …” In fact, these papers actually fine-tune on constructed non-triggering pairs of image and prompts to mitigate the memorization (overfitting) issue as per the training-time strategies, also they propose inference-time mitigation strategies that does not rely on the construction of prompt datasets. Both are quite practical, contrary to the paper's points.

### Questions
Please check out the weaknesses section, where the limited contribution and motivation are the major concerns that make me inclined to reject this paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MemBench, a benchmark for evaluating memorization mitigation methods in diffusion models. The core technical contribution is an MCMC-based sampling approach that efficiently finds prompts triggering generation of training data, building upon the memorization detection metric (Dθ) from Wen et al. (2024). The benchmark includes both memorized image trigger prompts and evaluation metrics to assess mitigation methods' effectiveness. The authors demonstrate their method finds substantially more trigger prompts than previous work and reveal issues with existing mitigation approaches. 

However, the paper's organization and presentation significantly obscure its contributions. The main technical innovation - using MCMC for efficient prompt sampling - is not clearly highlighted and is buried under various other aspects. The benchmark itself, while valuable, would benefit from clearer exposition of its components and limitations.

### Strengths
1. Novel MCMC-based approach for finding memorization triggers
2. Comprehensive evaluation framework for mitigation methods
3. Large-scale trigger prompt discovery
4. Practical insights into mitigation limitations
5. Not requiring training data

### Weaknesses
1. Critical Methodological Limitations:
   - The paper relies heavily on pre-trained language models (specifically BERT) for prompt sampling but fails to acknowledge this as a fundamental limitation. This is particularly problematic as such models have a training cutoff date (pre-2018 for BERT), making it impossible to find triggers containing newer terms or concepts. This temporal constraint severely limits the scope of the benchmark, potentially missing a significant portion of memorization cases related to more recent data. The method's reliance on a static vocabulary from a pre-trained model restricts its ability to discover triggers involving emerging trends, entities, or terminology.
   - The evaluation framework potentially misses a significant portion of memorization cases due to this temporal limitation. This is not just a theoretical concern; the inability to detect memorization of newer concepts could lead to an underestimation of the problem's scale and a false sense of security regarding the effectiveness of mitigation methods. The dependency on pre-trained language models restricts the generalizability of the method, making it difficult to apply to models trained on more recent or specialized datasets.

2. Unclear and Redundant Writing:
   - The paper's findings section contains three nearly identical statements that could be consolidated:
     Quote: "MemBench reveals several key findings:
     1. All image memorization mitigation methods result in a reduction of Text-Image alignment between generated images and prompts...
     2. The mitigation methods affect the image generation capabilities of diffusion models, which can lead to lower image quality...
     3. The mitigation methods can cause performance degradation in the general prompt scenario..."
     These are essentially making the same point about performance degradation, and this redundancy obscures the specific nuances of each finding.

   - The paper makes claims about metric superiority without proper justification:
     Quote: "while Ren et al. (2024) measured FID, the Aesthetic Score offers a more straightforward way to evaluate individual image quality and better highlight these issues."
     No evidence or explanation is provided for why Aesthetic Score is "more straightforward" or "better." The lack of comparative analysis or empirical justification for this choice weakens the argument for using the Aesthetic Score over established metrics like FID. Furthermore, the paper does not discuss the potential biases or limitations of the Aesthetic Score itself.

   - Key metrics are used without proper introduction:
     The paper extensively uses SSCD scores without ever explaining what they measure or their significance. This lack of explanation makes it difficult for the reader to understand the results and assess the validity of the conclusions. The paper should provide a clear definition and interpretation of the SSCD score, including its relationship to memorization detection.

### Questions
My main problem with the paper is the organization of the writing, I like the idea and I think it is novel, however writing does not focus on main contribution and lack to properly refrence some of the things I mentioned in weakness section

1. Language Model Limitations:
   - How do you address the temporal limitation of using BERT (trained pre-2018) for prompt generation? 
   - What percentage of potential memorization cases might be missed due to this limitation?
   - Have you considered using more recent language models or alternative approaches?

2. Methodological Clarity:
   - Could you provide specific details about the computational constraints that prevented certain comparison methods from being included in the main body of the paper not just in the appendix.
   - Can you clarify the source and context of the reported AUC values from Wen et al. 2024 in the main body of the paper?

3. Metric Choices and Evaluation:
   - What empirical evidence supports the choice of aesthetic score over FID? please also include FID in the paper

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
MemBench is a novel benchmark designed to evaluate image memorization issues in text to image diffusion models. This work includes a benchmark dataset that evaluates image memorization in text to image generation models (authors claim to be first). the benchmark itself contains comprehensive metrics on memorization. 

In addition to the benchmark itself, authors provided analysis of the effectiveness of various mitigation approaches.

### Strengths
The proposed MCMC-based search is a novel idea for quickly searching for problematic prompts.

The design of MemBench is well thought out and is comprehensive in its metrics for wide adoption.

### Weaknesses
The work uses Stable Diffusion 2 to show empirical evidence of memorization and how well their benchmark works. However, their proposal seems unable to apply to models like Stable Diffusion 3 (or other newer models than SD2) where training data is unknown. In Appendix D, the authors did not show may evidence of memorization of SD3. This makes me wonder how widely applicable this work is



### Questions
In Appendix D, the authors mention they cannot do reverse image search on SD3 generated images since its training set is unknown. Have you tried to reverse search on the LAION 5B dataset despite SD3 had no confirmation of using LAION 5B. Given the size and popularity of LAION, I would assume it (partially) overlaps with the training set of many modern text to image diffusion models.

### Soundness
2

### Presentation
3

### Contribution
2

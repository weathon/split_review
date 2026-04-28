# Revealing the Unseen: Guiding Personalized Diffusion Models to Expose Training Data

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Diffusion Models (DMs) have evolved into advanced image generation tools, especially for few-shot fine-tuning where a pretrained DM is fine-tuned on a small set of images to capture specific styles or objects. Many people upload these personalized checkpoints online, fostering communities such as Civitai and HuggingFace. However, model owners may overlook the potential risks of data leakage by releasing their fine-tuned checkpoints. Moreover, concerns regarding copyright violations arise when unauthorized data is used during fine-tuning.  In this paper, we ask: \textit{“Can training data be extracted from these fine-tuned DMs shared online?” } A successful extraction would present not only data leakage threats but also offer tangible evidence of copyright infringement. To answer this, we propose FineXtract, a framework for extracting fine-tuning data.  Our method approximates fine-tuning as a gradual shift in the model's learned distribution---from the original pretrained DM toward the fine-tuning data. By extrapolating the models before and after fine-tuning, we guide the generation toward high-probability regions within the fine-tuned data distribution. We then apply a clustering algorithm to extract the most probable images from those generated using this extrapolated guidance. Experiments on DMs fine-tuned with datasets such as WikiArt, DreamBooth, and real-world checkpoints posted online validate the effectiveness of our method, extracting approximately 20\% of fine-tuning data in most cases, significantly surpassing baseline performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a model guidance-based approach to fine-tuning data recovery, where it leverages the denoising prediction from pre-trained models $\epsilon_{\theta}$ to extrapolate the predictions from fine-tuned models $\epsilon_{\theta^{'}}$. The resulting denoiser can be used to sample data from a distribution similar to the fine-tuned data distribution $q$. The authors further extend this to text guidance diffusion models. After denoising steps, a clustering algorithm was applied to further improve the extraction accuracy. The experimentations demonstrate improved average similarity and average extraction accuracy of extracted images compared to text-to-image and CFG with clustering as baselines. Further ablation study was conducted to understand the impact of training images $N_0$ and generated images $N$, as well as model hyperparameters such as guidance scale $w'$ and correction term scale $k$. Results on possible defenses against the proposed method were also presented.

### Strengths
- The paper is well-written with clear presentations. For example, the method sections of model guidance and text-guidance extension are presented in a way that is easy to follow, and further details on caption extraction are elaborated in the appendix. The figures and tables are quite easy to parse and get the main results.
- The experimentations are quite comprehensive, with ablation studies on several important hyperparameters concerning models and datasets. 
- It is also very good to present some defenses against the proposed method and discuss the implications of these results

### Weaknesses
The main weaknesses are the task setup and the significance of results:
- For task setup, the paper seems to address a relatively clean form of fine-tuned models, whereas in real-world settings the pre-trained models might be not always available (sometimes presented with noisy labels), and in many cases, the fine-tuned model could be a mixture of multiple fine-tuned data distributions and pre-trained models. I wonder how the proposed methods were able to consider much more realistic scenarios.
- The main experiments are conducted on a relatively small test dataset that consists of 20 artist models (10 mages per model) and 30 object models (4-6 images per model), making the significance of results hard to judge. Moreover, the improvements over the two selected baselines are noticeable (table 1). When increasing $N_{0}$, the performance drops significantly (figure 4a), the model does not work very well on fine-tuned models with a larger scale of images. These results suggest space for improvements, which are all needed from this work considering the applications of real-world problems.

### Questions
1. Can you provide more intuition on eq (3)? For example, besides the training iterations effects on $\lambda$, how $\lambda$ might be affected by the size of fine-tuned data and their similarities?
2. What's the performance of extraction accuracy with increasing fine-tuning data $N_{0}$? 
3. Can you conduct more analyses on the impact of different combinations of DMs and training data (artistic styles vs. object). It seems their performance are quite different from table 1 and table 2.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel framework FineXtract to extract fine-tuning data from fine-tuned diffusion models' checkpoints. The authors approximate the learned distribution during the fine-tuning process of diffusion models and use it to guide the generation process toward high-probability regions of the fine-tuned data distribution. Besides, a clustering algorithm is proposed to extract images visually close to fine-tuning datasets. Experiments result on fine-tuned checkpoints on various datasets, various diffusion models verify the effectiveness of the proposed FineXtract.

### Strengths
1. The paper is overall clear written and easy to follow.
2. The paper focuses on extracting fine-tuning data from diffusion models' checkpoints. This research topic has not been paid attention before.
3. The code is available.

### Weaknesses
1. The experiment of the paper is not solid enough, the paper needs more experiments to verify the proposed method works. The paper only chooses "Direct Text2img+Clustering" and "Classifier Free Guidance + CLustering" as baselines. I think these two methods are only ablation counterparts. It is better to compare the proposed method with other relative works on extracting training/finetuning data.
2. The proposed method seems sensitive to the guidance scale $w'$ and correction term $k$. How to decide the hyper-parameters in practice might be challenging.
3. I am somewhat skeptical about the necessity of developing a dedicated method specifically for extracting images from the fine-tuning phase. It seems feasible to simply apply existing methods for extracting training images directly on the fine-tuned checkpoint, then filter out the results that overlap with images extracted from the pretrained model.

### Questions
Please see "Weaknesses".

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the data extraction problem of diffusion model, particularly focusing on the fine-tuning data. The authors use the parametric approximation of the distribution shift between the original model and fine-tuned model as guidance, to generate the fine-tuning data. Experiments across different diffusion models on various datasets and real-world checkpoints from huggingface demonstrate the effectiveness of proposed method.

### Strengths
1.	The focus on extracting fine-tuning data is indeed interesting. this focus reveals a new perspective on privacy concerns, which could enhance the security of diffusion models and preserve the privacy of data owners.
2.	The experiments are also conducted on checkpoints from real-world platform, i.e., huggingface, demonstrating the practical effectiveness of the proposed method.
3.	The paper is generally well-written, with a clear structure that is easy to follow.

### Weaknesses
1.	The performance of the proposed method keeps decreasing with the growth of training data. Will the growth of class number have the same effect? How can this issue be mitigated in practice, especially given the vast volume of training data used for industry diffusion models?
2.	The performance under LoRA fine-tuning is noticeably worse. Does this suggest that the proposed method is less effective for parameter-efficient tuning? 
3.	The effectiveness of the proposed method is significantly diminished when being attacked. The authors state that "transformations render ... images largely unusable." Could you provide statistics on the extent of unusability? To what degree does the attacker lose model utility to achieve the attack performance reported in Table 3?

### Questions
Please refer to Weaknesses.

### Soundness
2

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
3

### Summary
The paper proposed a framework FineXtract, which exploits the transition from the pre-trained DM distribution to the fine-tuning data distribution to accurately guide the generation process to the high-probability region of the fine-tuning data distribution, thereby achieving successful data extraction. Experiments on multiple datasets and real-world checkpoints, highlight the potential risks of data leakage and provide strong evidence for copyright infringement.

### Strengths
1. This paper is well-written.
2. This framework can be applied to both unconditional and conditional DMs.
3. The result is significant, highlighting the potential risks of data leakage.

### Weaknesses
1. In Sec. 5.2, the performance of baselines under various $N$ and $N_0$ deserves further discussion.
2. The reason why Correction Term Scale $k$ performs better in the negative case needs further analysis, which is inconsistent with its motivation.
3. It is worrying whether using PCA to extract important signals from multiple-words prompts is feasible when $W$ is large.
4. Some symbol errors, for example, the second $\epsilon_{0,77}$ in Appendix A.3 should be $\epsilon_{1,77}$.

### Questions
This paper is both interesting and innovative. However, there are some weaknesses that need to be improved. Please refer to Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

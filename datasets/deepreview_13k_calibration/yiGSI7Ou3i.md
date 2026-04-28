# Text-to-Model: Text-Conditioned Neural Network Diffusion for Train-Once-for-All Personalization

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
Generative artificial intelligence (GenAI) has made significant progress in understanding world knowledge and generating content from human languages across various modalities, like text-to-text large language models, text-to-image stable diffusion, and text-to-video Sora. While in this paper, we investigate the capability of GenAI for \textit{text-to-model} generation, to see whether GenAI can comprehend hyper-level knowledge embedded within AI itself parameters. Specifically, we study a practical scenario termed train-once-for-all personalization, aiming to generate personalized models for diverse end-users and tasks using text prompts. Inspired by the recent emergence of neural network diffusion, we present \textbf{\texttt{Tina}}, a text-conditioned neural network diffusion for train-once-for-all personalization. \texttt{Tina} leverages a diffusion transformer model conditioned on task descriptions embedded using a CLIP model. Despite the astronomical number of potential personalized tasks (e.g., $1.73\times10^{13}$), by our design, \texttt{Tina} demonstrates remarkable in-distribution and out-of-distribution generalization even trained on small datasets ($\sim 1000$). 
We further verify whether and how \Tina understands world knowledge by analyzing its capabilities under zero-shot/few-shot image prompts, different numbers of personalized classes, prompts of natural language descriptions, and predicting unseen entities. \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a new generative AI framework named Tina, which can generate "personalized" neural network models based on text prompts. This approach, called train-once-for-all personalization, enables a single model to generalize and create task-specific models on demand without the need to fine-tune the model on task related data. Tina leverages a diffusion transformer model conditioned on descriptions encoded with a CLIP model to understand and apply user-specific knowledge, even with a small training dataset. It demonstrates strong performance in generating models for both in-distribution and out-of-distribution tasks, supporting zero-shot and few-shot scenarios with images and adapting to different classification settings. The framework opens possibilities for text-to-model applications, expanding the range of personalization within neural network.

### Strengths
1. Comprehensive Experimental Analysis: The paper includes a robust set of experiments, covering different prompt types, model architectures, dataset sizes, and scaling laws. These analyses provide a clear understanding of Tina’s capabilities and boundaries, and they validate (to some extent) the model’s effectiveness in generating personalized networks under varying conditions.
2. Novel Approach to Model Personalization: The paper builds on the concept of train-once-for-all personalization, allowing a single pre-trained model (Tina) to generate personalized models dynamically based on text prompts. This can potentially eliminates the need for separate training per task, making the approach highly efficient and versatile.

### Weaknesses
1. The approach is not scalable. The experiments are not showing a possibility to scale the approach for larger number of classes (limited to 10) or for more complex models. The paper presents what seems like a good proof of concept but it would require more work to demonstrate the effectiveness of the approach on larger more complex problems.
2. The datasets used are too small and simple to validate the approach properly. 
3. One very important baseline that is missing is a direct fine tuning which should be an upper bound. The selected baselines are not representative enough to see what is the  loss in performance to expect with Tina.
4. The generic model in the experiments seems to be quite bad even on the in-distribution tasks. I would have expected it to perform better with improvements coming from Tina

### Questions
Nit: Please add a reference for the claim” We choose DiT as the backbone because it can be easily scaled up and is shown to have great
generalization and expressiveness.”  Line 210

In Table 3, it is not clear how many classes were predicted. This is important to assess the reported accuracies.

Can you please comment on how would you set the number of model parameters for new unseen tasks?

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
3

### Summary
This paper focuses on neural network parameter generation and utilizes diffusion models for text-to-model generation. With just one training session, the proposed method achieves outstanding results in both out-of-distribution and in-distribution model personalization.

### Strengths
1. It’s an interesting idea of using text-conditioned diffusion models to generate neural network parameters based on varying requirements. 

2. Extensive experiments have been conducted to validate the effectiveness of the method.

### Weaknesses
1. The proposed method is currently limited to personalizing models for image classification tasks. As a pilot study for generating neural networks with diffusion models, it does not fully support the title of "train-once-for-all." Conducting more experiments on detection and segmentation would enhance the overall credibility of the study.

2. The method can generate only a relatively small number of parameters—specifically, around 640 parameters in the classifier layers of ResNet-20. It still heavily relies on the feature extraction module of the generic model. Therefore, the significance of "text-to-model" is weakened if the partial model parameters are already provided.

3. The ablation of text prompts indicates that the proposed method is sensitive to the input prompt. Could training with mixed prompts improve the stability?

4. In traditional diffusion models, the inclusion of random noise could improve the diversity of the output. But it seems useless in the proposed method because the aim of Tina is to find the best classifier without considering diversity.

### Questions
see the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents Tina, a novel framework that leverages text-conditioned neural network diffusion for generating personalized models from textual prompts. It addresses the scenario of train-once-for-all personalization, aiming to create customized models for diverse end-users and tasks using text prompts. Tina is designed to generalize across in-distribution and out-of-distribution tasks, even with limited training data. The paper claims that Tina demonstrates an understanding of world knowledge by analyzing its capabilities under various conditions, including zero-shot/few-shot image prompts, different numbers of personalized classes, and predicting unseen entities.

### Strengths
- The writing is clear and easy to follow.
- The discussed topic and motivation are both innovative and significant.

### Weaknesses
- Though I'm not well-versed in the subject of this article, I'm still amazed by the "text-to-model" concept. I'm skeptical about the "train-once-for-all" approach since the author didn't provide any code or demos to back up the experimental results.

- What kind of experimental settings did Tina use in text-to-model task—simple or challenging? What are the limits of Tina's capabilities?

- I'm very curious whether the proposed Tina has theoretical support.

### Questions
see weakness

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigate the capability of GenAI for text-to-model generation, to see whether GenAI can comprehend hyperlevel knowledge embedded within AI itself parameters. The basic idea is to use diffusion transformers to generate parameter token by token. Each token is indeed a set of parameters in a specific layer. The model is trained with supervised learning approach to feed user-provided text description and then use diffusion model to synthesize the personalized network parameters. The results seem quite interesting.

### Strengths
1. The paper has solid technical contribution.
2. The proposed method is novel and clean.
3. The experimental results are also strong.

### Weaknesses
1. The writing of this paper need improvement. The introduction is quite obscure and high-level. It only shows some broad idea without elaborating the actual implementation much. I would suggest the authors to hint a bit in terms how they tokenize the parameters and use DDPM to predict the actual parameters, etc. This could help the authors gain more clear insights.
2. The evaluated datasets are still a bit toy or simple. The whole paradigm still requires more thorough or large-scale experiments to validate.

### Questions
The main difficulty for this prediction is its limitation to relatively small neural network. Assuming that we want to predict a 1B parameter transformer network, how would you address it?

### Soundness
3

### Presentation
3

### Contribution
3

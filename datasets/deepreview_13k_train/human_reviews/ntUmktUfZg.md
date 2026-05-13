# Generate to Discriminate: Expert Routing for Continual Learning

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
In many real-world settings, norms, regulations, or economic incentives
permit the sharing of models but not data across environments. 
Prominent examples arise in healthcare 
due to regulatory concerns. 
In this scenario, the practitioner wishes to adapt the model to each new environment
but faces the danger of losing performance on previous environments
due to the well-known problem of catastrophic forgetting. 
In this paper, we propose Generate-to-Discriminate (G2D), a novel approach that leverages recent advancements in generative models to alleviate the catastrophic forgetting problem in continual learning. 
Unlike previous approaches based on generative models 
that primarily use synthetic data
for training the label classifier,
we use synthetic data to train a domain discriminator.
Our method involves the following steps:
For each domain, (i) fine-tune the classifier and adapt a 
generative model to the current domain data;
(ii) train a domain discriminator to distinguish synthetic samples 
from past versus current domain data; 
and (iii) during inference, route samples to the respective classifier.
We compare G2D to an alternative approach, where we simply replay the generated synthetic data, and, surprisingly, we find that training a domain discriminator is significantly more effective than augmenting the training data with the same synthetic samples. We consistently outperform previous state-of-the-art domain-incremental learning algorithms 
by up to $7.6$ and $6.2$ points across three standard 
domain incremental learning benchmarks in the vision and language modalities, respectively,
and $10.0$ points on a challenging real-world dermatology medical imaging task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes tackles the setting of domain incremental learning by leveraging generative models as a routing mechanism. Specifically, for each task / domain $t$, the proposed approach
1. trains a domain specific expert $f_t$, 
2. finetunes a pretrained generative model trained on $(x,y)$ pairs from task $t$, 
3. trains a domain discriminator on the aggregated synthetic samples from all $t$ domains seen so far by sampling from the respective generative models. 
4. At test time, the domain discriminator infers the task from the query data, and fetches the appropriate domain expert to make a prediction. 

The authors evaluate the proposed method across four benchmarks, spanning both text and images, and real world medical imaging. Results show better performance than using the learned generative models for replay.

### Strengths
1. The approach is interesting; by decomposing the general domain incremental learning problem into (1) domain identification and (2) expert retrieval, the proposed approach is able to see performance gains. 
2. The approach provides a fresh perspective on the use of synthetic data for domain incremental learning, which is potentially less vulnerable to sub-par generated samples.

### Weaknesses
1. The authors fail to discuss the computational cost of the method. How is the task discriminator trained ? Is it trained from scratch at every new domain, or continually learned ? What is the training cost of having to train two additional models (task classifier and generator) compared to expert learning ? Specifically, the paper lacks a detailed breakdown of the computational overhead associated with training the domain discriminator and the generative model, including the number of parameters, training time, and memory requirements. This is crucial for assessing the practical applicability of the method, especially in resource-constrained environments.
2. How does this approach scale ? My understanding is that it does so poorly if the task discriminator is not trained continually. More generally, it seems that the authors don't quite understand the computational efficiency related to PEFT approaches; taking LoRA for example, the computational cost saved from not performing a gradient update step on the full parameters is quite small compared to the cost of having to compute forward and backward passes in the model. The "gains" from peft are really in parameter efficiency and serving of these models. Furthermore, the paper does not explore the potential bottlenecks in scaling the proposed method to a large number of domains or tasks. The computational complexity of training and inference with an increasing number of domain-specific experts and the associated discriminators needs to be addressed.
3. Relevance of the setting : The authors provide initial motivation of the setting in the paper, where model weights may be made available, but not the actual data used for training. I have trouble seing healthcare institutions open-sourcing generative models of their data, but not the actual data itself. I would appreciate if the authors could point me to such instances.

### Questions
1. T5 is an encoder decoder model, thus enabling conditional generation. How are you generating synthetic data from this model, i.e. where is the data fed to the encoder coming from ? Do you have a separate generator for this ? 
2. is the classifier at task t finetuned from task t -1 ? or finetuned from the pretrained model ?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed to address the domain-incremental learning problem by learning domain-specific models combined with a model capable of distinguishing between domains. This domain discriminator is trained using synthetic data from a continually fine-tuned generative model. An important empirical demonstration is that the authors show that this indirect approach (i.e., first identify the domain, then solve the problem) works better than when directly learning a model to solve the problem in all domains while replaying the same synthetic data sample.

### Strengths
I consider demonstrating that it can be more efficient to address a domain-incremental learning problem in an indirect way (i.e., G2D; first identify the domain, then solve the problem) than in a direct way (i.e., Generative Replay; directly learn to solve the problem in all domains) an important and insightful contribution.

### Weaknesses
Unfortunately, I think that the paper does not provide enough experimental details to properly assess whether the comparison between G2D and Generative Replay is performed in a fair manner. In particular, based on the provided details, it is unclear to me whether Generative Replay has been implemented in an optimal manner. Examples of details / explanations that should be provided:

- How is / are the classifier model(s) finetuned? In section 5.4. it is stated “we fine-tune only 1.04 ~ 2.5% of trainable parameters”. How was this percentage decided? How is it decided which parameters are fine-tuned? Is this approach of fine-tuning the same for the classifier models of G2D and the classifier model of Generative Replay?

- With Generative Replay, how are the loss on the replayed data and the loss on the data from the current task weighed? Are they simply added? Or are they balanced in such a way as to approximate the joint loss over all domains so far?


Could the authors explain why they took the S-iPrompts results from the Wang et al (2022a) paper, but not the S-liPrompts results?

On p5 towards the bottom the authors claim that ER with a limited buffer size is an upper bound for generative replay. This does not seem correct.

### Questions
Most importantly, the authors should provide full details regarding how the generative replay experiments were implemented in order for the reviewers to be able to judge whether the key comparison of this paper was performed in a fair manner.

Could the authors explain why they took the S-iPrompts results from the Wang et al (2022a) paper, but not the S-liPrompts results?

I would be happy to actively engage in the discussion period.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The authors suggest a new method for domain-incremental continual learning, leveraging recent approaches in conditional generative models. Specifically, the authors generated samples to train a domain discriminator which, in turn, is used as expert gate, to route samples at inference time to the appropriate expert model.
- Furthermore, the paper suggests a new benchmark dataset for domain-incremental learning, named DermCL, combining different dermatologic datasets.
- They evaluate their approach on 3 vision and 1 text (QA) tasks.

### Strengths
- The paper addresses a relevant topic, namely domain-incremental catastrophic forgetting. 
- The approach follows a simple and neat idea, which is to employ generated samples to train a gate model, instead of using them in an augmentation step to finetune the classification model.
- The authors provide a good summary of related work.
- The authors conduct extensive experiments with various datasets and multiple modalities (image, text).

### Weaknesses
 - It is hard to connect the table with the text -> e.g. in tab 1: where is ER? Whats CaSSLe? What’s the difference between G2D and G2D (Full FT) –> roughly explained much later in the text? Why are different methods compared for different (vision) datasets?

### Questions
- Will the new benchmark dataset be published?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

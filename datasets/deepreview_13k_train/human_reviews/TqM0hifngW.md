# Learning Video-Conditioned Policy on Unlabelled Data with Joint Embedding Predictive Transformer

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
The video-conditioned policy takes prompt videos of the desired tasks as a condition and is regarded for its prospective generalizability. Despite its promise, training a video-conditioned policy is non-trivial due to the need for abundant demonstrations. In some tasks, the expert rollouts are merely available as videos, and costly and time-consuming efforts are required to annotate action labels. To address this, we explore training video-conditioned policy on a mixture of demonstrations and unlabeled expert videos to reduce reliance on extensive manual annotation. We introduce the Joint Embedding Predictive Transformer (JEPT) to learn a video-conditioned policy through sequence modeling. JEPT is designed to jointly learn visual transition prediction and inverse dynamics. The visual transition is captured from both demonstrations and expert videos, on the basis of which the inverse dynamics learned from demonstrations is generalizable to the tasks without action labels. Experiments on a series of simulated visual control tasks evaluate that JEPT can effectively leverage the mixture dataset to learn a generalizable policy. JEPT outperforms baselines in the tasks without action-labeled data and unseen tasks. We also experimentally reveal the potential of JEPT as a simple visual priors injection approach to enhance the video-conditioned policy.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Video-conditioned policy learning often requires extensive action-labeled demonstrations, which are costly and time-consuming to acquire.  To address this problem, a method named Joint Embedding Predictive Transformer (JEPT) is introduced in this paper. JEPT jointly
learns visual transition prediction, which predicts the next visual state in a sequence based on the current observation and prompt video with unlabelled data, and inverse dynamics, which learns to infer actions that cause the transition between two states given the labeled data. The model is evaluated on two benchmarks, Meta-World and Robosuite, and is compared with recent state-of-the-art methods. Experimental results show that JEPT achieves superior performances.

### Strengths
- The paper is novel and addresses real-world problems. More specifically, decomposing the behavior cloning into visual transition prediction and inverse dynamics learning is novel, prior approaches mostly rely on labeled data or direct behavior cloning, while JEPT makes use of unlabelled data and largely improved generalization ability and performance.
- The experiments are solid and thorough. JEPT is compared with recent state-of-the-art methods. The robustness analysis and visual prior injection studies are interesting and inspiring.

### Weaknesses
 - The model’s performance appears sensitive to the choice of visual priors. It is unclear how to select desired priors across different environments, or when facing a new task how to choose the prior. The paper lacks a systematic analysis of how different visual priors affect the learned representations and downstream task performance. The current approach of injecting pre-trained visual encoders, while showing some promise, does not provide a clear methodology for selecting the appropriate prior for a given task or environment. This raises concerns about the practical applicability of the method, as users may struggle to determine the optimal visual prior without extensive experimentation.
- The paper primarily validates JEPT on simulated datasets. The paper can be improved by adding real-world datasets for more complex environments, strengthening the claims of generalizability and practical applicability. The reliance on simulated environments limits the assessment of the model's robustness to real-world variations, such as lighting changes, occlusions, and sensor noise. The absence of real-world experiments makes it difficult to ascertain whether the performance gains observed in simulation would translate to practical scenarios. This is a significant limitation, as the ultimate goal of many robotics tasks is to operate in real-world settings.

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
A training strategy for video-conditioned policy generation is proposed in this manuscript. Considering the challenge of annotating action labels, the author propose to split the behavior cloning task into two sub tasks to reduce the dependencies on annoatated data. The visual transition prediction task predicts the observation embedding of next time step in the feature space, and the inverse dynamics leanring task estimates the current action by taking the consecutive two observations of current time step. The training of the visual transition prediction needs only the prompt videos and expert videos without action annotation. The training of inverse dynamics learning requires the prompt video, the expert video and the corresponding annotations. This training strategy is quite similar to the popular strategy pre-training (visual transition prediction) + supervised learning (inverse dynamics learning) . The proposed method is evaluated on two benchmark datasets, the Meta-World task and the Robosuite task, and the experimental results show the effectiveness of the proposed mtehod.

### Strengths
1. The proposed method aims to introduce prompt video as guidance for task imitation learning, which is interesting.
2. The involvement of visual transition prediction for observation embedding prediction is good. It can not only help reduce the cost of action annotation, but also make the task easier to learn. The prediction of observation embedding in the next time step in feature space is easier than the direct embedding extraction from the raw observation of the next time step. However, the premise the embedding space is well learned.
3. The proposed method is extensively evaluated and achieves good performance.

### Weaknesses
1. The paper is not easy to follow, especially for the researcher not in the robotics field. A further polishment of the manuscript would be great

* The authors are suggested to clarify each term such as prompt video (which is used as a whole global representation in the method), expert video. A simple explanation would be apprecaited;
* Based on my understanding, the key design of the proposed method is the split of behavior cloning into two sub-tasks the visual transition prediction and the inverse dynamics leanring, which can help utilize the mixture dataset, and reduce the dependency on action annoataion. However, the authors did not discuss much on why this design works and why it is suitable for the situation when the annotation of actions is limitted;

2. From the view of pretraining, a well pre-trained network needs tremendous unlabelled data to fit a good network. For video/image understanding, the requiremenet of large-scale data is easy to fullfill. However for the robotics task, the large-scale data is relatively diffcult to acquire.

3. Considering the diversity of robot configuration, the action state or the description of action in each robot is differernt. This paper does not mention how to handle the heterogeneity issue among robots, which limits the scenario span of the proposed method.

### Questions
1. How to handle the heterogeneity issue? Is the action space designed for only one robot configuration?
2. What is the ratio of $D_{demo}$ and $D_{vid}$ in the mixture dataset? From the view of model pretraining, does the $D_{vid}$ require much more samples than $D_{demo}$? How the ratio influence the final performance? An involvement of the ablation study on the ratio would be appreciated.
3. Is the hyperparameter $c$ in Eq.9 also influenced by the ratio of $D_{demo}$ and $D_{vid}$?
4. Considering $E_{prt}$ is a global representation of the prompt video, it would be interesting to see how $E_{prt}$ of videos from different action categories distribute in the feature space. Ideally, there should be high differentiation among the $E_{prt}$ from different action categories such that the model will not be misled by the guidance from $E_{prt}$.

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
3

### Summary
the paper propose Joint Embedding Predictive Transformer (JEPT), where the model can be conditioned on some video based demonstations, and the causal transformer also learns to predict the next action and observation (in pixels) space. The prompt video encoder, can be used to give demonstactions just from a video, this is great because giving an intertion is hard with language, and even babies do this from visual demonstations. The JEPA style video model, encodes causally the state and actions, and the joint encoder maps actions to states and there are jointly optimized during training. The paper evaulates these models on various benchmarks, and shows good performance.

### Strengths
The main stength of this paper is to able to prompt the robot from simple visual demonstrations. This has very nice benifits from not having any dependcy from langauges and from development physcology it make sense, as babies learn/ and repeat actions by watching others.  

The paper has through experiments on meta world and robosuit, and in most of the cases the performance is good compared to previous works. 

Ablations also clearly shows the benifits of joint embedding model.

### Weaknesses
more qualititative samples might be also helpful to see the experiments in action, and to show how the rollout of actions and h_t changes over time. 

Lack of any real world examples is one weakness, it would be nice if the paper can show these nice propeties of giving a simple video demo, and the robot can mimic it in real world setting, that would be great, and can also answer many questions regarding the usefullness of the work. 

It would be also nice, if the paper can address how the patch tokens are encoded, and how they are handled during the autoregresive stage of the pollicy.

### Questions
please look at my strengths and weakness sections, and if you can adress the weakness section, i am happy to change my ratings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the Joint Embedding Predictive Transformer (JEPT), a novel approach for video-conditioned policy learning that leverages both expert demonstrations and expert videos paired with prompt videos to reduce the need for action label annotation. To effectively learn from the mixture datasets, JEPT decomposes the learning task into two subtasks: visual transition prediction and inverse dynamics learning. By jointly training these subtasks, JEPT enhances the generalization of the video-conditioned policy. Experimental results demonstrate that JEPT outperforms baseline methods.

### Strengths
1. The proposed JEPT framework for learning from mixed datasets is clear and reasonable.
2. Experiments on the Meta-World and Robosuite benchmarks demonstrate the effectiveness of JEPT.
3. Results indicate that visual priors can be integrated into JEPT to improve generalization.

### Weaknesses
1. Does BC+IDM train both the video encoder and the inverse dynamics model on demonstration videos? What if a fixed pretrained video encoder is used instead? This could ensure that the representations of demonstration and expert videos are in the same space, potentially aiding in the learning of generalizable actions.
2. How does JEPA influence performance? Did the authors experiment with other pretrained models, including different architectures and pretrained data?
3. The comparison of different visual prior injection methods appears inconsistent. The four models rely on distinct visual signals as inputs, which has led the authors to conclude that optical flow is the most suitable prior. However, these models were trained on different datasets and under varying conditions (self-supervised or supervised). It is crucial to detail these differences, as they may influence the performance.

### Questions
1. Does BC+IDM train both the video encoder and the inverse dynamics model on demonstration videos? What if a fixed pretrained video encoder is used?
2. How does JEPA influence performance? Did the authors experiment with other pretrained models, including different architectures and pretrained data?

### Soundness
3

### Presentation
3

### Contribution
3

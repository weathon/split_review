# Fast-ELECTRA for Efficient Pre-training

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
ELECTRA pre-trains language models by detecting tokens in a sequence that have been replaced by an auxiliary model. 
Although ELECTRA offers a significant boost in efficiency, its potential is constrained by the training cost brought by the auxiliary model. Notably, this model, which is jointly trained with the main model, only serves to assist the training of the main model and is discarded post-training. This results in a substantial amount of training cost being expended in vain. To mitigate this issue, we propose Fast-ELECTRA, which leverages an existing language model as the auxiliary model. To construct a learning curriculum for the main model, we smooth its output distribution via temperature scaling following a descending schedule. Our approach rivals the performance of state-of-the-art ELECTRA-style pre-training methods, while significantly eliminating the computation and memory cost brought by the joint training of the auxiliary model. Our method also reduces the sensitivity to hyper-parameters and enhances the pre-training stability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes efficient pretraining with ELECTRA by using a fixed generator (auxiliary model) instead of training the aux model together with the discriminator for replace token detection (RTD). In order to simulate a curriculum of difficulty that training of aux model provides, it uses an exponentially decaying schedule on the *temperature* used to sample from aux model.

Efficiency: Since the aux model is fixed, Fast-ELECTRA saves on backward passes leading to overall 20-30% FLOPs per step. (This calculation ignores original training of the auxiliary model.) It also saves 20-25% memory in the aux model. One could also cache the aux model predictions and save a lot more FLOPs (30-40%).

Quality: Fast-ELECTRA is competitive with many BERT and ELECTRA related baselines, even slightly better on some GLUE downstream evals

Robustness: The paper evaluates robustness to curriculum schedule and discriminator model size, and finds that Fast-ELECTRA behaves more gracefully compared to ELECTRA and can handle higher learning rates.

The paper also performs interesting ablation studies with using some simple aux models and different (linear/poly) schedules for curriculum. Overall, the paper presents a conceptually interesting finding that that a fixed pretrained aux model can be used, with a temperature schedule. Incomplete comparisons to earlier ideas made it harder to judge novelty

### Strengths
Novelty: The idea of using a fixed aux model for efficiency is interesting, and novel to my knowledge (although I'm not entirely sure since I could not find much discussion about this). Similarly the idea of using decaying temperature as a curriculum in this context is quite interesting

Quality: The paper provides a nice analysis of computation and memory benefits of the method.

Clarity: The paper is easy to follow for most part. Connections to prior work and some other details could be presented better.

### Weaknesses
Comparison to prior work:

- It would be helpful to highlight the most relevant work in Table 1 that a reader should focus in. Additionally, is there any evaluation on prior work that uses fixed generator? It would also help to include some FLOPs comparison to the baselines used in Table 1. The paper will also help with a discussion on accuracy-efficiency tradeoff. Lack of such discussions made it harder to assess the full value of proposed method.

- Recent paper (Dong et al.) from ICML 2023 proposed a different strategy of decoupling generator and discriminator optimizers and has better GLUE metrics than Fast-ELECTRA. This does not dilute the contributions of this paper much because Fast-ELECTRA also leads to training speed up, and is conceptually different. However it will be helpful to include and compare to this method. It could be an interesting open question if the gap to Dong et al. can be reduced with a fixed aux model.


Missing discussions: Most of the paper assumes the existence of a good pretrained aux model, but ignores the cost of training the aux model itself. Does Fast-ELECTRA truly reduce total FLOPs in that case?

### Questions
- In Eq 2 what is the range of $u$? What is the final temperature in that case? If $u$ is indeed fraction of training updates, then at the max value of $u=1$ the final temperature has a value different from 1. Is that intended?

- Section 3 says “the auxiliary model expends about 67% of the computation cost” If aux model is just 1/3 the size, why does it contribute so much to computation cost?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a simple and effective technique to improve electra training. By replacing the training of the auxiliary model with a pre-trained model together with temperature scaling and a gradually decreased temperature, the proposed method significantly reduced the memory usage and training time of electra training.

### Strengths
1. Simple and effective method.
2. Good performance.
3. Very clear presentation.

### Weaknesses
The scale of models in experiments seems a bit limited under the current standard. Have you tried larger models?

### Questions
See weakness.

### Soundness
3 good

### Presentation
4 excellent

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
This paper explores efficient ELECTRA training methods by advocating the use of a pre-trained/existing language model as an auxiliary model, rather than simultaneous training of the model and auxiliary model.

### Strengths
1. The method is both intuitive and effective.
2. The problem it tackles is highly practical.

### Weaknesses
1. The proposed method appears tailored specifically for ELECTRA, potentially limiting its applicability and community interest.
2. Could we consider applying a continual learning method (e.g., [1]) to enhance ELECTRA's efficiency?

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

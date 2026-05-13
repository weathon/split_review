# Patch-Level Training for Large Language Models

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
The prohibitive training costs of Large Language Models (LLMs) have emerged as a significant bottleneck in the development of next-generation LLMs. In this paper, we show that it is possible to significantly reduce the training costs of LLMs without sacrificing their performance. Specifically, we introduce patch-level training for LLMs, in which multiple tokens are aggregated into a unit of higher information density, referred to as a `patch', to serve as the fundamental text unit for training LLMs. During patch-level training, we feed the language model shorter sequences of patches and train it to predict the next patch, thereby processing the majority of the training data at a significantly reduced cost. Following this, the model continues token-level training on the remaining training data to align with the inference mode. Experiments on a diverse range of models (370M-2.7B parameters) demonstrate that patch-level training can reduce the overall training costs to 0.5$\times$, without compromising the model performance compared to token-level training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper seeks to reduce the training cost of LLMs by using patch-level training in the initial stage. A patch consists of multiple consecutive tokens, and patch-level representation can reduce training costs due to shorter sequence representations. Experiments performed across four model sizes and six NLP tasks show that the proposed method can reduce training costs by up to 50% with little to no performance degradation.

### Strengths
1. Reducing LLM training costs is an important research question. The problem formulation, motivation, and improvement objective of the paper are clear.

2. The proposed method is described clearly, and there seem to be adequate details to reproduce the work. The cost reduction of the proposed training method is significant and robust across multiple LLM sizes and NLP tasks.

3. The experiments cover a wide range of settings such as the fraction of patch-level training (lambda), patch size (K), model size, etc.

### Weaknesses
1. The optimal hyperparameters and intuitions derived from the work may be very specific to the settings associated with the paper. For example, the optimal values of lambda and patch size may be sensitive to the tokenizer. Therefore, the improvements of the proposed work may not generalize similarly to a new tokenizer. Specifically, the interaction between the patch size, the vocabulary size of the tokenizer, and the resulting information density within each patch is not thoroughly explored. A tokenizer with a larger vocabulary might result in different optimal patch sizes compared to a tokenizer with a smaller vocabulary, and this is not addressed in the current analysis. Furthermore, the paper does not discuss how the patch-level training might affect the model's ability to handle subword tokenization, which is crucial for handling out-of-vocabulary words and morphological variations.

2. It is not obvious whether the patch-level pretraining is suitable for larger scales. There are issues with training stability and convergence that only occur when the model size is scaled to several billions. The paper lacks a discussion on how the proposed method might affect the training dynamics at larger scales, such as the potential for increased variance in gradients or the need for different optimization strategies. The authors should consider the potential for instability when scaling to larger models, as the patch-level training might introduce additional challenges in terms of convergence and generalization.

### Questions
N/A

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
4

### Summary
This work introduces a novel pretraining scheme aimed at reducing computational cost of pretraining. The core idea is to reduce the effective length of training sequences by concatenating and averaging the token representation of mutliple tokens into a patch representation. Then the model predicts tokens from the next patch using the output representation of the next patch. The simplicity of this idea is very intriguing as it does not require any extra parameters in the model. After such path-level pretraining with higher efficiency authors go back to tokenlevel training in order to ensure that the model will adjust to next token prediction representation.

Authors completed experiments showing that their method scales well with larger models and supports both streaming and multi-epoch training scenario. Extensive benchmarking showed that models trained with their approach are cheaper to train and are better or on the same level of performance as baseline models.

### Strengths
1. the method is easy to implement and brings original contribution, i see it being used a lot in the community and industry if it will pass the proof of concept in real world scenario.
2. High quality experiments cover wide range of model sizes and data settings. In addition, wide range of benchmarks are covered to evaluate the final model performance compared with usual token level training.
3. Assuming that this approach would scale with even larger models, this work provides a significant contribution in the pretraining research.

### Weaknesses
 * Unclear conclusions about the effect of architecture. In the architecture ablation the observations are suggesting that there are might be some use cases where subsequent token level training does not work very well. IMO this might be important to highlight better in the text to avoid overselling the method.
* No numbers showing the actual speed improvements. Since all token projections are computed in patch level training, the expensive softmax operations over vocabularies have to be done. So it is interesting what is the speed improvement factor as we change K (patch size) in practice on real hardware. It is not clear if the speedup comes from reduced sequence length or from some other factor.

### Questions
* Following my last weakness point, did you measure the speed up coming from patch level training in practice? e.g. in tokens per second metric or so. This would be very interesting to know.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents an interesting approach to accelerate the costly pre-training of language models. The core idea is to change the basic unit from a token to patch which comprises several tokens. This results in computational savings for the main transformer model (the input encoding and the model prediction still produces tokens but it does so based on a patch encoding).

### Strengths
The paper presents an interesting approach to accelerate language model training, specifically:
* the approach appears to be novel
* the paper is well written and clear in the presentation
* the approach is thoroughly evaluated (different (small) model sizes, including an array of ablations, an alternative approach to computing patches etc.)

### Weaknesses
 * The evaluation is on the smaller scale of language mode sizes. Evaluation for larger model sizes is very challenging but it would be a large plus to understand the scalability of the method.
* Table 3/4 show PPL results and draw conclusions based on the difference between PPLs in the range of ~10 and later on in ~7. This assumes that PPL is a linear measure but it is in fact an exponential quantity based on cross entropy. Therefore, the actual entropy difference between PPL 11 and PPL 10 is far lower than it is between, say PPL 8 and PPL 7. I would encourage the authors to simply report entropy instead of PPL for this particular analysis to make this clearer.
* Line 266 mentions that the context length in the patch level training has little effect. Using context length KT performed as well as just T. However, these conclusions were drawn based on a very small model with 370M parameters which may not be able to exploit the larger context as well as higher capacity models. Did you perform a comparison on a larger model?
* Does the patch level training objective have any notion of which token position is currently being predicted within a patch (eq 3)? It appears to treat a patch as a bag of words with no order? This would be interesting to contrast with a setting where there is a notion of order.
* Section 3.5 analyses the patch size K and deems K=2/4 to have a good speed/accuracy tradeoff in your setting which is a two-stage procedure: (1) train with some K>1 and then (2) use K=1 at the end of training. However, you could also consider a more general setting where there are many more stages and where where you start with very large K and then progressively decrease K until you end up with K=1. Have you considered this?

### Questions
* Line 266 mentions that the context length in the patch level training has little effect. Using context length KT performed as well as just T. However, these conclusions were drawn based on a very small model with 370M parameters which may not be able to exploit the larger context as well as higher capacity models. Did you perform a comparison on a larger model?
* Does the patch level training objective have any notion of which token position is currently being predicted within a patch (eq 3)? It appears to treat a patch as a bag of words with no order? This would be interesting to contrast with a setting where there is a notion of order.
* Section 3.5 analyses the patch size K and deems K=2/4 to have a good speed/accuracy tradeoff in your setting which is a two-stage procedure: (1) train with some K>1 and then (2) use K=1 at the end of training. However, you could also consider a more general setting where there are many more stages and where where you start with very large K and then progressively decrease K until you end up with K=1. Have you considered this?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a strategy to reduce training cost of LLMs using patch level training, where 'patch' refers to a sequence of consecutive tokens. The key idea is to perform training at the patch level initially whereby prior patches are used to predict the next patch, and then proceed with regular token level training.  The paper applies the approach to a range of model sizes (370M-2.5B) and shows that it can reduce the training cost by 50% without any performance degradation on model perplexity or downstream task performance. The paper presents variation in performance wrt patch size, model size, amount of training data and multi-epoch scenarios.

### Strengths
* Presents a simple approach to reduce training cost using a patch level training for initialization the regular token-level training
* Reports experiments on a range of model sizes showing that the approach can reduce training cost by 50% without any degradation in model performance

### Weaknesses
 * There are some parts of the paper which are unclear. See questions below.
* It would be good to see some additional analysis/ablations to understand why the approach can lead to performance improvements.
* L156: "Instead, we maintain a single output head and make its prediction cover all tokens in the next patch". How is this done? Does your output vocabulary have a size of K*|V| where |V| is the number of symbols ?
* Equation 3 uses 'p' to refer to both probabilities and patches. Consider using different symbols for the two.
* Sec 3.7: Have you run experiments adding more transformer layers for mapping the token embeddings to patch embeddings and vice-versa at the output side? It is possible that a linear mapping is not powerful enough.

### Questions
* L156: "Instead, we maintain a single output head and make its prediction cover all tokens in the next patch". How is this done? Does your output vocabulary have a size of K*|V| where |V| is the number of symbols ?
* Equation 3 uses 'p' to refer to both probabilities and patches. Consider using different symbols for the two.
* Sec 3.7: Have you run experiments adding more transformer layers for mapping the token embeddings to patch embeddings and vice-versa at the output side? It is possible that a linear mapping is not powerful enough.

### Soundness
4

### Presentation
3

### Contribution
4

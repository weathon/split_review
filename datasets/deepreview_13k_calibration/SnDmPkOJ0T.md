# REEF: Representation Encoding Fingerprints for Large Language Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 10, 8, 6, 8

## Abstract
Protecting the intellectual property of open-source Large Language Models (LLMs) is very important, because training LLMs costs extensive computational resources and data. Therefore, model owners and third parties need to identify whether a suspect model is a subsequent development of the victim model. To this end, we propose a training-free REEF to identify the relationship between the suspect and victim models from the perspective of LLMs' feature representations. Specifically, REEF computes and compares the centered kernel alignment similarity between the representations of a suspect model and a victim model on the same samples. This training-free REEF does not impair the model's general capabilities and is robust to sequential fine-tuning, pruning, model merging, and permutations. In this way, REEF provides a simple and effective way for third parties and models' owners to protect LLMs' intellectual property together.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper aims to protect LLM's IP by identifying the relationship between the suspect and victim models from the perspective of LLMs’ feature representations. This paper proposes REEF that identifies whether a suspect model is derived from a victim model, given the representations of these two models on certain examples.
The similarity between representations is quantified using Centered Kernel Alignment. 
Empirical evaluations of this paper consider:
- Victim model: Llama-2-7b
- Suspect model: quantization and fine-tuned variants of Llama-2-7b as well as unrelated models

### Strengths
1. The proposed approach REEF 
 - Is training-free, simple and efficient 
 - Does not impair the model’s general capabilities 
 - Is robust to sequential fine-tuning, pruning, model merging, and permutations
 - Is intuitive as feature representations of fine-tuned victim models are similar to feature representations of the original victim model, while the feature representations of unrelated models exhibit distinct distributions

2. Experimental evaluation 
 - considers an informed adversary who is aware of the proposed approach REEF and tries to evade the detection. This paper creates that adversary through the designing of a customized loss function that maximises the representational divergence between models. Results in Appendix D indicate that such fine-tuning seriously damages the model’s general capabilities and renders the fine-tuned models unusable.
- considers comparison with baselines: Weight-based Fingerprinting Methods and Representation-based Fingerprinting Methods
- considers robustness to fine-tuning, pruning, merging, permutation and scaling transformation

### Weaknesses
I enjoyed reading this paper, and I am happy with the current version as it has already considered all important studies in its theoretical and empirical analyses. Below, are a few suggestions which could improve the paper further:   
1. This paper creates that adversary by designing a customized loss function that maximises the representational divergence between models. Is there any more effective way to create such an informed adversary? For example, designing a better loss function or performing other operations?
2. This paper studies the impact of sample numbers on the performance of REEF. However, there is no evaluation of the type of data points for a given number of samples. Can the performance of REEF be improved if we select/generate samples in a specific way instead of random sample selection? 
3. This paper considers one single family of LLMs as a victim model. Generalization of results to other families of victim models would be interesting. 
4. One of the observations of this paper is that "CKA from a single layer is sufficient for fingerprint identification." In order to relax the assumption of requiring access to intermediate representations of models for the proposed approach, how much does the detection performance degrade if we use only the last layer?

### Questions
See my above questions regarding instantiating the informed adversary, the type of selected examples, generalisation of your results to other families of LLMs as victims, and relaxing the requirements of having access to intermediate representations for detection.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes REEF, a scheme for identifying “suspect” models that were derived from “victim” models. REEF does not require modifying the training process at all. The key idea of REEF is to measure the similarity between the feature representations of the two models. They first consider training a classifier to do so, however they observe that this approach is not robust. Their actual scheme instead computes a more robust similarity metric, called the centered kernel alignment, between the two models. This metric still captures similarity of the feature representations, but is robust to permutations. This work includes a comprehensive suite of experiments showing that REEF is robust to standard attacks such as permutation and pruning attacks.

### Strengths
This paper appears to be original, taking the known idea that models develop distinct feature representations, and introducing a novel use of the central kernel alignment score to measure similarity between these representations robustly. The scheme does not require changing the training algorithm of the original model, which is a nice property.

This paper is clearly written and well organized. The experiments are comprehensive in comparing the REEF scores of several known models, considering various practical attacks. The experiments also compare REEF to several existing fingerprinting schemes.

The result appears to be a significant incremental improvement. That is, REEF is a slightly more robust fingerprinting scheme than existing schemes. It does not introduce profoundly new ideas, but has solid practical improvement.

### Weaknesses
The biggest weakness is that REEF does not offer any provable false positive guarantee. Furthermore, this work does not measure the false positive rate, and indeed it is challenging to measure the false positive rate in a meaningful way since real-world LLMs are so expensive to train. Although this work does compare the REEF scores of several models, this sample size is not enough to extrapolate a false positive rate in general. For example, it is unclear how REEF would perform on two models that are independently trained on similar datasets– would REEF assert that one model is stolen from the other? The false positive rate is especially important if one wants REEF scores to be used to accuse a party of stealing a victim model.

It would also be interesting to see what happens when a model is fine-tuned to minimize its REEF score with the model it is derived from.

### Questions
How does REEF perform on models that were independently trained on the same (possibly publicly available) dataset? Is there a risk of false positives here?

How does one measure the false positive rate in general?

### Soundness
3

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
2

### Summary
The paper proposes to use CKA to measure the independence between two representations of two LLMs as the model fingerprints. Proposed issue is aiming to address the challenges brought by model pruning, model merging, and other techniques that can change the model architecture to make prior fingerprint detection useless. The experiments show the effectiveness of the proposed method.

### Strengths
- Protection of the IP of the large language model is an urgent and important topic.

- The experiments are extensive to show the effectiveness of the proposed method.

- The authors clearly identify the challenges and limitations of existing fingerprint methods.

### Weaknesses
The novelty is limited in replacing similarity measures of the prior work. There is a lack of theoretical analysis of proposed methods. Additionally, I'm confused about the first heatmap of Figure 6. It shows that the two LLMs trained on different datasets will have a high CKA similarity, which will lead the REEF to classify them into the same model. This means all models using the same architecture but trained by different datasets will share the same fingerprint. It doesn't make sense.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method to identify descendant models of a large language model by using a kernel-based similarity measure between the descendants and the original model. This similarity measure enables robust similarity computation and effective detection of descendant models. However, the proposed method is only effective in a white-box scenario where the parameters of both the potential descendant models and the original model are publicly accessible. The detection performance using this similarity calculation is high and robust.

### Strengths
- S1: The paper is well-organized and easy to follow.
- S2: The proposed method identifies descendant models of a large language model through kernel-based similarity with the original model, allowing for robust and effective discovery of descendant models.
- S3: The method is intuitive and well-supported by analytical study.

### Weaknesses
 - W1: The security model and fingerprint verification setting are not clearly defined. The proposed method is only effective in a white-box scenario where the parameters of both the descendant models and the original model are publicly accessible. To avoid misunderstandings regarding potential applications in black-box scenarios, such as through API access, the paper should clarify the security model, including the verifier’s capabilities. Specifically, the paper should detail the exact information available to the verifier, such as access to model weights, intermediate activations, or only input-output pairs. The current description lacks the necessary detail to assess the practical applicability and limitations of the method.
- W2: The proposed fingerprint verification method is limited to direct descendant models of the original “root” model and is not designed for verifying claims from these descendants against further generations. This limitation is significant for the proposed fingerprint verification approach. The paper should explicitly state this limitation and discuss its implications for real-world scenarios where models may undergo multiple stages of fine-tuning or adaptation.

### Questions
Address W1.

### Soundness
4

### Presentation
3

### Contribution
3

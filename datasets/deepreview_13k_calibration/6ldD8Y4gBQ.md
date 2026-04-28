# Data Taggants: Dataset Ownership Verification Via Harmless Targeted Data Poisoning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Dataset ownership verification, the process of determining if a dataset is used in a model's training data, is necessary for detecting unauthorized data usage and data contamination.
Existing approaches, such as backdoor watermarking, rely on inducing a detectable behavior into the trained model and on a part of the data distribution.
However, these approaches have limitations, as they can be harmful to the model's performance, require unpractical access to the model's internals.
Furthermore, previous approaches lack guarantee against false positives.\\
This paper introduces \textit{data taggants}, a novel non-backdoor dataset ownership verification technique, specifically designed for image classification datasets.
Our method uses pairs of out-of-distribution samples and random labels as secret \textit{keys}, and leverages clean-label targeted data poisoning to subtly alter a dataset so that models trained on this dataset respond to the key samples with the corresponding key labels.
The keys are built as to allow for statistical certificates with black-box access only to the model.\\
We validate our approach through comprehensive experiments on ImageNet1k using ViT and ResNet models with state-of-the-art training recipes.
Our findings demonstrate that data taggants can reliably identify models trained on the protected dataset with high confidence, without compromising validation accuracy.
We show the superiority of our approach over backdoor watermarking in terms of performance and stealthiness.
Furthermore, our method exhibits robustness against various defense mechanisms from data poisoning literature, accross different architectures, and dataset modifications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces data taggants, a novel non-backdoor dataset ownership verification technique that helps detect if machine learning models were trained using a specific dataset. Unlike previous approaches that rely on backdoor watermarking, data taggants use pairs of out-of-distribution samples and random labels as secret keys, and employs clean-label targeted data poisoning to subtly alter a small portion (0.1%) of the dataset. When models are trained on the protected dataset, they respond to these key samples with corresponding key labels, allowing for statistical verification with only black-box access to the model. The authors validate their approach through comprehensive experiments on ImageNet1k using Vision Transformer and ResNet models, demonstrating that data taggants can reliably detect models trained on the protected dataset with high confidence, without compromising validation accuracy. The method proves to be stealthy, robust against various defense mechanisms, and effective across different model architectures and training recipes. It also provides stronger theoretical guarantees against false positives compared to previous approaches.

### Strengths
1. Use out-of-distribution samples as keys is quite novel.
2. Provides stronger statistical guarantees than previous work.
3. Well-structured methodology presentation.

### Weaknesses
1. Lacks formal security analysis against adaptive attacks.
2. No investigation of downstream task impacts

### Questions
1. How does the method defend against an adversary who knows the exact verification technique?
2. Why was 0.1% chosen as the modification budget, and how sensitive is the method to this choice?
3. Have you investigated potential negative effects on downstream tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an active dataset ownership verification (DOV) method, by adapting a technique for targeted data poisoning from prior work. The key advantages of the proposed approach are its applicability given only top-k black-box access, more principled/rigorous statistical certificates compared to prior work, stealthiness, and robustness to different setups as well as explicit defenses. All these properties are validated via thorough experimental evaluation.

### Strengths
- DOV is an important problem, and authors explicitly focus on realistic setups and often overlooked aspects such as the rigor of stated guarantees that accompany methods.
- The method is original within the space of DOV. The idea of repurposing witches brew and introducing random data sampling to strengthen the theoretical guarantees is very interesting and unexpected. 
- Evaluation focuses on a large-scale practical setup and addresses many important points, evaluating stealthiness and robustness explicitly. I appreciate the inclusion of poisoning defenses and OOD detection. 
- Setting the scope of evaluation aside (see below), the provided results seem quite strong.
- The paper is mostly well-written and easy to read, with some exceptions discussed below.

### Weaknesses
I can identify several important weaknesses of the work in its current state, and provide suggestions how these could be improved:
- **Incomplete evaluation/related work positioning**: While DOV is a crowded space and many baselines are cited in the paper, only two are run in the experimental part, without clear rationale, and the relationship to prior methods is in my view not clearly presented in the paper. For example, while the position of the paper seems to be "there may be DOV methods with strictly better TPR but they come with problems such as unrigorous guarantees or perceptible data changes", current Table 1 shows Taggants are the best even when only measuring TPR, which to me suggests that baselines are missing. The field is complex and there are many dimensions (active vs passive, blackbox top-k vs needs logits vs needs whitebox, different guarantee types, clean label vs perceptible, etc.). To give clarity, I believe the paper must (i) clearly outline all dimensions and place all prior baselines within them (ii) include any viable baseline (e.g., a perceptible method can be still run to demonstrate that even though it achieves high FPR, it fails a data poisoning defense) and clearly state why the others can not / should not be included. This would greatly improve the trust in the experimental results and make the case for Taggants.
- **Unclear claims of technical contribution**: The paper should clearly mark that many technical parts are directly lifted from Witches Brew (e.g., augmentations, restarts), while some other parts are introduced by this work (e.g., the use of random data, perceptual loss). The current writing can easily be interpreted as an overclaim, esp. by a reader not familiar with prior work. The actual contributions are quite interesting, and I do not think the lack of tech. contribution is a weakness of the paper in any case.
- **Unsubstantiated claims around guarantees**: One of the key claimed advantages of Taggants are rigorous guarantees not offered by prior work, as (i) random data samples are actually independent and (ii) under the null, the classifications of random data are actually uniform. While I tend to agree on an intuitive level, I believe (1) the reasons why prior work violates (i,ii) could be more clearly explained, e.g., ln301 simply states that "using model's predictions on ground truth class" violates the independence assumptions, but does not elaborate; (2) to show actual impact of this oversight of prior work, it should be empirically demonstrated that there is a mismatch between theoretical and empirical FPR (3) for taggants, there should be a corresponding matching FPR empirical validaiton, and a more detailed discussion around why taggants do not break the assumptions. Are model predictions on random [0,1]^d data really uniformly random? All these images are unusually high-variance compared to natural data; if we had a class such as "TV static" I can imagine they would all be classified as such? Do we need a different OOD distribution in this case, and how would we choose it? This needs more clarity as it is quite central to the paper.
- **[Minor] Key technical contribution undexplored**: If I understand correctly, the motivations given for how Keys are sampled are more rigorous guarantees as above, and lower likelihood to alter model utility, as data is OOD. However, Table 3 also shows forcing the model to predict a certain class is easier in this case than for in-distribution test images. If am not misinterpreting Table 3, it would be interesting to know why this is the case, and state it as the third reason for using such Key sampling to avoid confusion. Is it that gradient matching is here a better proxy for the true objective, or the objective is easier to optimize as we are far from the real data manifold? This seems underexplored but is a central idea of the paper.

Typos and points that do not affect my evaluation:
- ln151: dot missing, ln518: extra dot, ln188: extra "them". ln317: "In each experiment..." sentence seems wrong, not sure where.
- Related work says "[Data/model] watermarks are not designed to persist through processes that use the data", but I am not sure this is really the case, as these watermarks are generally designed with the goal of robustness. There are works that show (albeit on text) explicitly that such watermarks can persist through processes of finetuning and RAG (see Sander et al. "Watermarking Makes Language Models Radioactive" and Jovanovic et al. "Ward: Provable RAG Dataset Inference via LLM Watermarks")---this discussion could be included to give context. On a similar note, the data/model/backdoor watermarks distinction could be made clearer, e.g. by changing the first paragraph title in Sec. 2.

I am happy to hear from authors regarding these points and discuss them further.

### Questions
- Optimization is done only w.r.t. fully trained model parameters. Yet, the goal of the gradient matching is to make training a model from scratch on Taggants equivalent to training it on Keys. Why are some randomly initialized models not included? Do you have insight why despite this, the surrogate objective seems to work? 
- How should tau=0 on ln317 be interpreted? If I understand correctly, this means all models with non-zero accuracy on Keys are flagged?

### Soundness
2

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
4

### Summary
The paper proposed a dataset ownership verification method that can work in a black-box setting, where model weights and training details are not known in advance; Besides, the method is also stealthy compared to the backdoor-based method since it only requires limited perturbations to the dataset; Moreover, the method is also less harmful than the previous backdoor-based method.

### Strengths
- The proposed method focuses on harmlessness, stealthiness, and black-box, which are three important challenges in the ownership verification problem.
- The writing is easy to understand and follow.

### Weaknesses
 - Novelty issues: Could you compare this paper with [1] in more detail, such as technical details, setting, and problem setup? Since in my understanding, [1] used a similar gradient-matching-based method to find some "hardly generalized domain", which is very similar to this method on a high level.
- Unclarified arguments: In Lines 59-60, the authors mentioned that 'but is also harmful to the model as it introduces errors [1]'. Could you further clarify what kind of errors the backdoor-based method introduces? In my personal understanding, the claim of "harmless" in [1] is mainly based on the fact that the backdoor-based method will leave exploits in the dataset, which will then further be maliciously used by the adversaries.
- Unclarified intuitions: The intuitions on why the "out-of-distribution" samples are used to construct key images are not further clarified.
- Experimental Details: Why do you choose SleeperAgent as the backdoor method for the baseline "Backdoor watermarking"? SleeperAgent is not the simplest way to inject backdoors and even requires an additional surrogate model to optimize perturbation $\delta$ to the original dataset. Therefore, could you (1) further clarify what is the necessity of choosing SleeperAgent, (2) provide more explanations on why the backdoor watermarking only achieves 0 TPR on your setting, and (3) provide additional experiments on the Backdoor watermarking with BadNet?

### Questions
See the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper, the authors propose Data Taggants, a dataset ownership method used to detect unauthorized data usage. Data Taggants relies on clean-label targeted data poisoning technique and requires only black-box access to the suspected model. Data Taggants generate secret keys, i.e., (input label) pairs, and signed input samples by maximizing the alignment between keys and signed samples, and induce a certain behavior only on the models trained by the modified version of the dataset including those signed images. The verification procedure of Data Taggants include statistical tests using suspected model's top-k predictions on the secret key.

I think there is novelty, particularly considering the application, but an incremental one as Data Taggants use ideas from gradient matching (Geiping et al. 2020).

### Strengths
1. Empirical results show that Data Taggants have zero false-positive rate and high true positive rate while maintaining the model performance. 
2. The generation of secret keys is purely random and is not included in the modified dataset, which makes key recovery almost impossible and unique to the data owner. 
3. The presentation is clear.

### Weaknesses
1. As far as I understand, the verification includes querying the suspected model with keys. As they are purely random and out-of-distribution, the adversary might evade the verification by trying to detect those specific inputs and altering the predictions. Specifically, an adversary could implement an out-of-distribution (OOD) detector, which is a standard technique in machine learning, to identify the random keys. Upon detection, the adversary could then modify the model's behavior on these inputs, for example, by forcing the model to output a uniform distribution over classes, thereby effectively neutralizing the taggant. This would be a relatively straightforward attack, especially if the keys are generated from a simple distribution such as uniform noise. 
2. The method might be prone to watermark collusion: the adversary can generate its own key set and data taggants by modifying the already signed dataset, and after that it can also claim that the accuser is the malicious one. This is a significant concern because it undermines the uniqueness and reliability of the proposed ownership verification method. If an adversary can easily create a conflicting set of taggants, the entire system becomes vulnerable to disputes and false accusations. The lack of a robust mechanism to resolve such conflicts is a major weakness. 
3. Data Taggants has limited effectiveness and robustness when k=1 in top-k predictions. This is because the verification process relies on statistical tests of the top-k predictions, and when k is small, the statistical power of these tests is significantly reduced. This makes the method less reliable in scenarios where only the top prediction is available or considered.

### Questions
1. The radioactive data (Sabrayrolles et al., 2020) method has the option of black-box verification. In black-box verification, the radioactive data method compares the difference in loss between clean and radioactive images, and it does not necessarily involve training a student model to replicate the suspected model, it just checks the difference between the loss. Thus, authors' claim in page 1, line 053 as well as in page 3 lines 127-129 are incorrect. I strongly recommend changing the explanation. 
2. I do not understand why the authors think that the independence of observations assumption does not hold in statistical testing. The models' predictions are independent of each other in the inference phase. 
3. The authors empirically show that the data taggants are visually imperceptible, as designed in the methodology. It can work quite nicely on images with a large input space, but my question is how imperceptible this noise will be in data with lower-dimensional input spaces, e.g., smaller images like CIFAR10, gray-scale images or on a different data type like tabular data or text? 
4.  In Table 1, the authors show that the backdoor watermarking (Li et al., 2023) has zero TPR and zero FPR. How authors measured such drastic numbers when the reference reports much better numbers? Is it because backdoor watermarking uses the full probability set instead of top-k labels or due to the mechanism of Wilcoxon-test? 
5. What happens if the adversary decides to use a subset of the dataset? It will negatively affect the verification as the ratio of signed images to the whole dataset might decrease. Another case is how the performance of Data Taggants is affected when the adversary combines different datasets to train its model? The budget B will decrease and smaller budget produce worse results according to Table 3. 
6. Page 2, line 148: typo while giving the reference

### Soundness
3

### Presentation
3

### Contribution
2

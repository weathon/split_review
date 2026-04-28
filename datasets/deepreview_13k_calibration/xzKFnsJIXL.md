# Tighter Privacy Auditing of DP-SGD in the Hidden State Threat Model

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
\looseness=-1 \newtxt{Machine learning models can be trained with formal privacy guarantees via differentially private optimizers such as DP-SGD. In this work, we focus on a threat model where the adversary has access only to the final model, with no visibility into intermediate updates. In the literature, this ``hidden state'' threat model exhibits a significant gap between the lower bound from empirical privacy auditing and the theoretical upper bound provided by privacy accounting. To challenge this gap, we propose to audit this threat model with adversaries that \emph{craft a gradient sequence} designed to maximize the privacy loss of the final model without relying on intermediate updates. Our experiments show that this approach consistently outperforms previous attempts at auditing the hidden state model. Furthermore, our results advance the understanding of achievable privacy guarantees within this threat model. Specifically, when the crafted gradient is inserted at every optimization step, we show that concealing the intermediate model updates in DP-SGD does not amplify privacy. The situation is more complex when the crafted gradient is not inserted at every step: our auditing lower bound matches the privacy upper bound only for an adversarially-chosen loss landscape and a sufficiently large batch size. This suggests that existing privacy upper bounds can be improved in certain regimes.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In the "hidden state" threat model for DP-SGD, an adversary does not have access to intermediate updates and can see only the final model. This paper proposes to audit the hidden state threat model for DP-SGD by introducing adversaries who select a gradient sequence offline (i.e., ahead of when training starts) in order to maximize the privacy loss of the final model even without access to the intermediate models.

### Strengths
* The problem setting and results are really interesting and open up new avenues for future work. Identifying different regimes where the gap (between the new auditing lower bounds and the theoretical upper bounds) vanishes and where the gap remains is a nice contribution.
* The paper flows nicely and is and enjoyable to read.
* Simplicity is a virtue and I think the design of the gradient-crafting adversaries for privacy auditing is clever yet also intuitive.

### Weaknesses
 * The paper uncovers some interesting empirical results but doesn’t offer up much explanation for them. E.g. for regimes where there is a gap, we don’t really get an explanation as to why this gap exists. I do feel that this work falls short of its goal to “enhance our understanding of privacy leakage” (line 537) by reporting the results without interpretation. I think that including more discussions like the “high-level explanation” starting at line 373 would help round out the paper and provide more concrete directions for future work.
* Considering this is one of its main contributions, I found that the description of the adversaries and the privacy auditing scheme in the main paper is vague and not presented with full details.
* There might not exist a worst-case datapoint that can saturate the gradient clipping threshold at every iteration. Would it be possible to discuss what it means to breach the privacy of a datapoint that does not exist and may in fact be unrealizable?
* It seems like an adversary who could control the sequence of gradients would also be able to infer from that something about the intermediate models. Is this OK for the hidden state threat model?
* Is there any intuition behind privacy amplification only seems to occur for smaller batch sizes?
* Does Implication 1 say anything beyond what Implication 2 says? If the batch size is as large as possible (the entire dataset), then every datapoint will be included in every optimization step of DP-SGD?

### Questions
* There might not exist a worst-case datapoint that can saturate the gradient clipping threshold at every iteration. Would it be possible to discuss what it means to breach the privacy of a datapoint that does not exist and may in fact be unrealizable?
* It seems like an adversary who could control the sequence of gradients would also be able to infer from that something about the intermediate models. Is this OK for the hidden state threat model?
* Is there any intuition behind privacy amplification only seems to occur for smaller batch sizes?
* Does Implication 1 say anything beyond what Implication 2 says? If the batch size is as large as possible (the entire dataset), then every datapoint will be included in every optimization step of DP-SGD?

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
3

### Summary
This paper proposes a tighter privacy auditing bound by extending gradient-crafting (GC) models to the hidden state regime, where only the last iteration is released. By combining the GC technique with advanced privacy auditing methods, such as privacy auditing using 
$f$-DP, the authors achieve a refined privacy auditing bound for the hidden state model.

### Strengths
This paper applies GC models to audit various regimes, including both small and over-parameterized models. Additionally, different deep learning architectures (CNN, ResNet, FCNN) are evaluated in the experiments. Overall, the empirical results are convincing.

### Weaknesses
The main weakness of this paper is that it does not introduce a new privacy auditing method; rather, it extends the existing gradient-crafting method to the hidden state regime. The primary technical contribution appears to be constructing a sequence of gradients without requiring knowledge of the intermediate gradients at each iteration.

My question is about the $f$-DP part. In Remark 3, the authors claim that the approximation error from using the central limit theorem (CLT) can be ignored. However, the CLT may underestimate privacy when mixture distributions arise due to shuffling or sub-sampling [A]. For this reason, Nasr et al. (2023) adopt numerical methods, such as FFT, to calculate the privacy profile. For the hidden state model, an 
$f$-DP guarantee is provided by [B] without relying on the CLT.

Given these considerations, the authors' assertion that the CLT approximation error can be ignored may not be universally applicable, especially in scenarios involving mixture distributions in (shuffled) DP-SGD. A simple explanation in the main part might be beneficial to the readers.

### Questions
My question is about the $f$-DP part. In Remark 3, the authors claim that the approximation error from using the central limit theorem (CLT) can be ignored. However, the CLT may underestimate privacy when mixture distributions arise due to shuffling or sub-sampling [A]. For this reason, Nasr et al. (2023) adopt numerical methods, such as FFT, to calculate the privacy profile. For the hidden state model, an 
$f$-DP guarantee is provided by [B] without relying on the CLT.

Given these considerations, the authors' assertion that the CLT approximation error can be ignored may not be universally applicable, especially in scenarios involving mixture distributions in (shuffled) DP-SGD. A simple explanation in the main part might be beneficial to the readers.

[A] Unified Enhancement of Privacy Bounds for Mixture Mechanisms via f-Differential Privacy. Wang et al., NeurIPS, 2023.

[B] Shifted Interpolation for Differential Privacy. Bok et al., ICML, 2024.

### Soundness
4

### Presentation
4

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
This paper studies the auditing of last iterate privacy guarantees of DP-SGD for non-convex loss functions. Authors propose an auditing method where a canary gradient is introduced to the DP-SGD steps. Two methods for crafting this "worst-case" canary gradients is proposed: 1. a random direction in the parameter space is selected and a gradient of norm C is inserted to the mnibatch of gradients and 2. the adversary simulates the DP-SGD run and picks as the canary gradient the least updated dimension, again with norm C. Authors demonstrate empirically that if the canary is inserted at every iteration, the auditing bounds correspond to the DP accounting upper bounds, suggesting that the hidden state model does not necessarily provide additional privacy protection. When the canary is inserted less frequently, the adversaries power decreases. Finally, authors propose an auditing setting where the adversary inserts the crafted gradient only in the first iteration and controls the loss landscape. In this setting the auditing bounds match closely the DP bounds when minibatch used in DP-SGD is sufficiently large.

### Strengths
Auditing DP algorithms is an interesting and important line of work. Previous work, both in auditing and privacy accounting, have suggested that hiding the intermediate iterations of DP-SGD can be beneficial for the privacy guarantees. In this work, authors improve the privacy auditing of non-convex loss functions, by carefully selecting gradient canaries that get inserted for to the DP-SGD gradient sum. The proposed method significantly improves the existing methods, suggesting that the previous methods have not optimally used the threat model allowed by the hidden state setting.

Authors also study the amplification by iteration effect, by proposing a novel technique that introduces a crafted gradient only for the first step of DP-SGD. The empirical results for this study suggest that there might not be any amplification by iteration for certain non-convex losses, and that only the noise introduced by subsampling the data makes distinguishing the crafted gradient more difficult.

### Weaknesses
In general the paper is very well written and the arguments are easy to follow. However, I get a bit confused on the discussion regarding accounting in the section 5.1. Since the threat model studied does not benefit from the subsampling amplification, I don't see any reason of using PRV accounting. When there is no subsampling, the privacy analysis could be performed tightly with Gaussian DP or Analytical Gaussian accounting (Balle et al 2018).

The proposed method assumes that the crafted gradient is possible under the particular loss function. While I do believe that this might be the case for highly over-parametrized models, it would be great if authors could discuss this further in the paper. Would it be possible to somehow trace back the worst-case sample from the worst-case crafted gradient? Similarly the assumption that the adversary can craft the loss landscape to make the crafted gradient the most distinguishable could warrant further discussion.

### Questions
- It seems that the privacy accounting upper bounds remain the same for various k (Figures 2 and 3). Now, is this because you have actually accounted only the 250 iterations the canary was inserted? Or do you display the auditing results only up to $T=250$ iteration?
- I don't think there is any reason to use PRV as there is no subsampling. You could just use analytical Gaussian and obtain tight privacy bounds (instead of the upper and lower bounds you get from PRV).
- Caption of Fig4: "Figure 4a gives the ...", I guess you mean 4b?

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
3

### Summary
This paper proposes a privacy auditing method for DP-SGD under a hidden state threat model. Assuming an arbitrary non-convex loss function, the authors abstract away the specific design of neighboring datasets and directly construct gradient sequences for auditing. Their main difference from previous work, which audits DP-SGD with gradient-crafting adversaries at each step, is that they ensures that the gradient sequence is predetermined and not influenced by intermediate outputs, i.e., the sequence is decided offline before training.

The authors considers two types of gradient-crafting:

1. **Random-biased dimension:** randomly selects a dimension and crafts the gradient with the largest possible magnitude in that dimension.
    
2. **Simulated-biased dimension:** simulates the training algorithm, identifies the least updated dimension, and crafts gradients with the largest possible magnitude there.
    

Experimentally, they demonstrate that when a canary gradient is inserted at each step, their empirical privacy estimates are tight for common model architectures, including ConvNet, ResNet, and FCNN. The auditing also remains tight when the canary is periodically added with a periodicity of 5. However, at a periodicity of 25, the auditing for some settings may not be tight, suggesting possible privacy amplification by iteration. To investigate this, the authors conducted experiments, showing that their auditing is tight when the batch size and $\epsilon$ are large. This supports prior findings which shows DP-SGD on non-convex problems does not exhibit privacy amplification by iteration. Thus, relaxing the threat model to a hidden state model does not offer better privacy guarantees for certain non-convex problems.

### Strengths
1. The paper is clearly written and easy to follow.
2. The proposed method is simple yet empirically effective.
3. The empirical results provide insights into the settings (batch size and $\epsilon$) where DP-SGD may exhibit privacy amplification by iteration for non-convex problems.

### Weaknesses
Firstly, the conclusion of this work is not new: the main takeaway—that for some non-convex problems, the hidden state threat model does not lead to better privacy analysis for DP-SGD (i.e., no privacy amplification by iteration)—is the same as the conclusion in previous work [Annamalai, 2024]. However, the methodologies differ: [Annamalai, 2024] constructs a worst-case non-convex loss function for DP-SGD where information from all previous iterates is encoded in the final iterates, while this work directly constructs gradient sequences.

My other concern with this work is that its methodology is also quite limited, though it may be slightly more general than previous approaches (e.g. [Annamalai, 2024]). This work abstracts away the specifics of the loss function and model architecture, focusing directly on gradient crafting. While this simplification aids in designing canary gradients, it resembles a worst-case analysis across all non-convex problems. From a specific gradient sequence, it is not possible to deduce the corresponding loss function and model architecture on which DP-SGD is performed. As a result, the findings do not clarify which specific architectures and loss functions (i.e., types of non-convex problems) may or may not exhibit privacy amplification by iteration.

### Questions
The simulated biased dimension method appears quite similar to gradient crafting at each step in terms of implementation [Nasr et al., 2023]. What are the specific differences between these two methods?

### Soundness
2

### Presentation
3

### Contribution
2

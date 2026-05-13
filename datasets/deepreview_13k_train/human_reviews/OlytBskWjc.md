# Reinforcement learning on structure-conditioned categorical diffusion for protein inverse folding

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Protein inverse folding—that is, predicting an amino acid sequence that will fold into the desired 3D structure—is an important problem for structure-based protein design. Machine learning based methods for inverse folding typically use recovery of the original sequence as the optimization objective. However, inverse folding is a one-to-many problem where several sequences can fold to the same structure. Moreover, for many practical applications, it is often desirable to have multiple, diverse sequences that fold into the target structure since it allows for more candidate sequences for downstream optimizations. Here, we demonstrate that although recent inverse folding methods show increased sequence recovery, their “foldable diversity”—i.e. their ability to generate multiple non-similar sequences that fold into the structures consistent with the target—does not increase. To address this, we present RL-DIF, a categorical diffusion model for inverse folding that is pre-trained on sequence recovery and tuned via reinforcement learning on structural consistency. We find that RL-DIF achieves comparable sequence recovery and structural consistency to benchmark models but shows greater foldable diversity: experiments show RL-DIF can achieve an foldable diversity of 29\% on CATH 4.2, compared to 23\% from models trained on the same dataset. The PyTorch model weights and sampling code are available on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on inverse folding, i.e., recovering a residue sequence that would fold into a given 3D backbone structure. The key motivation for the paper is specifically to improve diversity of generated sequences. The method consists of a discrete diffusion model that is then fine-tuned using RL (policy gradient) to improve foldability (sc-TM). Evaluation includes a number of baseline methods, including ProteinMPNN, PiFold, etc.

### Strengths
The paper is clearly written and the evaluations are fairly extensive, involve a number of relevant baselines, and seem conducted with care.

### Weaknesses
The proposed method is largely a direct combination of available techniques. Discrete diffusion component seems to be a variant of GradeIF/D3PM with small changes, and the RL fine-tuning is based on the rather straightforward policy gradient method (e.g.) from Black et al. I don't really see generalizable methodological innovations. Of course, it's fine to mix and match methods with adjustments to produce a well-performing technique but then the paper rests on its empirical results.

I think it would be better to replace eq (8) with a measure calculated only within foldable sequences so as to separate foldability from diversity (so they can be assessed separately and together). Diversity was taken as the key motivation for the paper but the two notions (diversity and foldability) are now mixed together in the proposed metric. E.g., the downward slope in Figure 2 is in part just due to the fact that higher folding threshold automatically decreases the value of the current metric. Figure 2 can also give a wrong impression that RL-diff increases diversity since the metric can be improved by increasing foldability instead. In fact, the reward used for fine-tuning the diffusion model is sc-TM so tailored to increase foldability (not control diversity).



### Questions
The expectation after eq (3) should really be a sum

q(S_t|S_{t-1},v) should be q(S_{t-1}|S_t,v) in eq (9) 

In the model architecture, line 183, do you mean p(s_0|s_t) rather than p(s_{t+1}|s_t) as currently written? 

Table 1 would be easier to read if summarized in terms of curves. For example, calculate diversity within all generated samples from a method that pass a sc-TM threshold and then vary this threshold.

### Soundness
3

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
This paper introduces RL-DIF, a novel reinforcement learning-driven model for protein inverse folding, addressing the need for generating diverse ensembles of amino acid sequences that fold into specific, target 3D protein structures via inverse folding. Authors introduce a framework they call RL-DIF that applies a categorical diffusion approach pre-trained on sequence recovery, followed by reinforcement learning (RL) fine-tuning to optimize structural consistency. This two-phase training strategy enables RL-DIF to improve "foldable diversity"—the diversity of sequences that maintain the correct fold—while retaining sequence recovery and structural accuracy. In tests on CATH 4.2 and other datasets, RL-DIF achieved up to 29% foldable diversity, outperforming prior models, which peaked at 23%.
Key contributions of the paper include:
RL-DIF Model: A diffusion-based model refined with denoising diffusion policy optimization to balance diversity and structural fidelity.
Benchmarking Results: Demonstrating RL-DIF’s superior foldable diversity on multiple datasets.
Methodological Advancements: Introducing foldable diversity as a new metric to assess inverse folding model quality.
The RL-DIF model code and PyTorch weights are available in HF.

### Strengths
Paper tables an important problem in inverse folding with an interesting solution in the combination of diffusion model and RL. It's an exciting contribution that could open up a new set of metrics for inverse folding models. The diversity of inverse folding models is a known problem in practice, but few direct attacks have been taken. The authors develop an interesting approach that shows improvement on sequence diversity metrics relative to base line models.

### Weaknesses
The paper feels close to the acceptance threshold for me. However,I felt the authors could do a bit more. The increase in seq diversity generated by RL-DIF is modest in some cases. The authors could provide (A) more information on the trade off between structural similarity and sequence diversity along the training trajectory (b) More information on how hyper parameter can be used to relax structural similarity constant to increase diversity (c) exploration of regularization strategies like entropy based regularization to increase the diversity of sequences generated about the gains shown. (d) validation of structural similarity of generated sequences via alpha fold.

### Questions
Could the authors could provide (A) more information (plots) on the trade off between structural similarity and sequence diversity along the RL training trajectory (b) More information on how hyper parameter can be used to relax structural similarity constant to increase diversity (c) exploration of regularization strategies like entropy based regularization to increase the diversity of sequences generated about the gains shown. (d) validation of structural similarity of generated sequences via alpha fold.

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
5

### Summary
The paper presents RL-DIF, a discrete diffusion model trained for protein inverse folding and further fine-tuned on structural consistency. RL-DIF achieves comparable sequence recovery and structural consistency to existing methods, while having a better foldable diversity, beneficial to downstream optimizations.

### Strengths
- The proposed method combines recent advances in discrete diffusion and reinforcement learning alignment methods to improve the sequence diversity of protein inverse folding, an essential task in protein biology.
- The paper is easy to follow, and the experiments on various protein datasets show the improvement in diversity with the proposed method.

### Weaknesses
 - The novelty of RL-DIF is limited. Several existing papers utilize discrete diffusion models for protein inverse folding, for example, [1] and [2]. The idea of using structural consistency to fine-tune the inverse folding model has been explored in ESM3[3], although with language model as the base model. While the authors highlight specific modifications to the architecture and training process, these appear to be incremental improvements rather than fundamental innovations. The core idea of combining discrete diffusion with reinforcement learning for inverse folding, followed by structural consistency fine-tuning, is not entirely novel.
- The motivation for fine-tuning the model with structural consistency to improve the sequence diversity is not very clear. This is also reflected in the experiments in Table 1, where DIF-Only achieves higher diversity in most datasets except CATH-short and CATH-single. The authors state that the motivation is to improve structure quality, but the connection between structural consistency and sequence diversity remains unclear. It seems that the structural consistency fine-tuning is more about improving the quality of the inverse folding given a certain diversity level, rather than directly improving diversity itself.
- The Foldable Diversity is only calculated based on 4 generated sequences for each protein structure, which can have high variance. It is better to use a higher number of generated sequences, and report the standard deviation of the results across random seeds. Besides, it is also helpful to provide the ratio of the generated sequences that satisfy the sc-TM score constraint to give some idea of to what degree the Foldable Diversity is affected by the structural consistency. The current analysis does not provide a clear picture of the trade-off between diversity and structural consistency.
- The model is compared to only non-diffusion based inverse folding baseline methods. A comparison with diffusion-based methods [1,2] is missing. Given that the proposed method is also based on discrete diffusion, it is crucial to compare against other diffusion-based methods to properly assess its performance and advantages. The lack of such comparison makes it difficult to evaluate the contribution of the proposed method.
- Hamming distance is used to measure sequence diversity. However, it may not be able to capture the high-level diversity between sequences, which is more related to protein functions and more useful in practice. Thus, the distance calculated in a pretrained embedding space (eg. ESM embedding) could be better. Hamming distance only captures the number of different amino acids, but it does not account for the similarity between different amino acids, which is important for functional diversity.

### Questions
- How are the temperature values for the pretrained models selected? In Table 1, T=0.1 is much better than T=0.2 and T=0.3 for all baselines. How do they perform with a smaller T, eg. T=0.05 or T=0.01?
- The reviewer understands that it is computationally expensive to train RL-DIF on the same amount of data as ESM-IF. For a rough comparison, how is the performance of ESM-IF trained on the same dataset as RL-DIF-100K?

### Soundness
2

### Presentation
3

### Contribution
2

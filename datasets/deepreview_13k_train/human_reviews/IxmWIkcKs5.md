# A Simple yet Effective $\Delta\Delta G$ Predictor is An Unsupervised Antibody Optimizer and Explainer

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
The proteins that exist today have been optimized over billions of years of natural evolution, during which nature creates random mutations and selects them. The discovery of functionally promising mutations is challenged by the limited evolutionary accessible regions, i.e., only a small region on the fitness landscape is beneficial. There have been numerous priors used to constrain protein evolution to regions of landscapes with high-fitness variants, among which the change in binding free energy ($\Delta\Delta G$) of protein complexes upon mutations is one of the most commonly used priors. However, the huge mutation space poses two challenges: (1) how to improve the efficiency of $\Delta\Delta G$ prediction for fast mutation screening; and (2) how to explain mutation preferences and efficiently explore accessible evolutionary regions. To address these challenges, we propose a lightweight $\Delta\Delta G$ predictor (Light-DDG), which adopts a structure-aware Transformer as the backbone and enhances it by knowledge distilled from existing powerful but computationally heavy $\Delta\Delta G$ predictors. Additionally, we augmented, annotated, and released a large-scale dataset containing millions of mutation data for pre-training Light-DDG. We find that such a simple yet effective Light-DDG can serve as a good unsupervised antibody optimizer and explainer. For the target antibody, we propose a novel Mutation Explainer to learn mutation preferences, which accounts for the marginal benefit of each mutation per residue. To further explore accessible evolutionary regions, we conduct preference-guided antibody optimization and evaluate antibody candidates quickly using Light-DDG to identify desirable mutations. Extensive experiments have demonstrated the effectiveness of Light-DDG in terms of test generalizability, noise robustness, and inference practicality, e.g., 89.7$\times$ inference acceleration and 15.45\% performance gains over previous state-of-the-art baselines. A case study of SARS-CoV-2 further demonstrates the crucial role of Light-DDG for mutation explanation and antibody optimization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this study, a transformer-based model utilizing protein structural information is proposed to predict the change in binding free energy of protein complexes (antibodies). The simpler architecture of their model as compared to the previous SOTA, allows for faster exploration of fitness landscape in the antibody design task. Their model trained with data augmentation, and teacher guidance by the previous SOTA (prompt-DDG) has been shown to have better performance in the prediction of change in binding free energy.

Additionally, a novel Mutation Explainer algorithm, utilizing the predictions of their transformer-based model, is proposed to score the marginal benefit of each mutation per site. In an application to SARS CoV-2, their algorithm is shown to be better than generative or energy-based models in ranking known effective mutants, and better than conditional generative models in optimizing antibody mutants against SARS CoV-2.

Their evaluations are accompanied by comprehensive ablation study on the choice of teacher model, inclusion of data augmentation, knowledge distillation and structural information in the training of predictive model.

### Strengths
1. Generated an augmented SKEMPI-v2 dataset using previous SOTA model predictions on random mutations performed on SKEMPI-v2 annotated dataset. The augmented dataset was used for pretraining of their model.

2. Demonstrating the utility of an effective predictor of delta binding free energy in antibody optimization and screening, i.e., mutant selection, without the need for generative modeling.

3. Extensive benchmark on delta binding free energy prediction and ablation study on various design choices including type of teacher model, data augmentation, knowledge distillation and protein structural information.

### Weaknesses
1. Limited performance evaluation on anti-body design/optimization tasks.

2. A discussion on how their prior based design can be combine with other techniques, such as generative modeling to improve antibody design

3. Brief explanation as to why the bar is low (based on the range of correlation values in the tables) in the prediction of delta binding free energy.

### Questions
1. In the experiments of Table 6, the generated antibody mutants with different strategies are evaluated by the delta binding free energy predictor used to design the mutation explainer. This may not be a fair comparison, as it is kind of expected for the mutation explainer to perform well evaluated by the same predictor as the one that it is built upon. 
I understand that the ground truths are not available, however the performance evaluation should be independent of the model design.

2. I am curious to know if you have examined the transfer from single to multiple site mutations in the prediction of delta binding free energy? if yes, how do the current models perform? This is a question of interest in protein property prediction tasks using mutagenesis datasets.

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
4

### Summary
This paper introduces Light-DDG, a lightweight ΔΔG predictor for protein-protein interactions, with a focus on antibody optimization. The authors address the challenge of efficient mutation screening by developing a simpler architecture that achieves faster inference while maintaining predictive performance through two key techniques: (1) knowledge distillation from more complex models like Prompt-DDG, and (2) supervised pre-training on an augmented dataset (SKEMPI-Aug) they create and release.
The main contributions include:

- A lightweight Transformer-based ΔΔG predictor that achieves 89.7× faster inference compared to state-of-the-art models
- A large-scale augmented mutation dataset (SKEMPI-Aug) containing ~640k annotated samples for supervised pre-training
- An approach for explaining mutation preferences using iterative Shapley value estimation
- *in silico* Experimental validation showing competitive or improved performance across multiple metrics, including per-structure Pearson correlation and RMSE
- A case study demonstrating the model's application to SARS-CoV-2 antibody optimization

The authors demonstrate their method's effectiveness through *in silico* experiments, including ablation studies examining the impact of knowledge distillation and data augmentation, as well as analyses of structural noise robustness and architectural applicability.

### Strengths
1. Demonstrates effective application of augmentation and knowledge distillation to achieve significant inference speedup (89.7x) while maintaining or improving accuracy
2. The simplified architecture enables interpretable explainability results (Figure 6)
3. Shows promising results for combining architectural simplification with performance improvements through principled use of ML techniques

### Weaknesses
1. **Dataset and Baseline Comparison Issues**
   The paper's central claims about performance improvements are undermined by inconsistent dataset usage across baselines. The ablation studies clearly demonstrate the outsized impact of the dataset choice, yet there is no clear indication that all baseline models were trained on equivalent data. This makes the comparative results in Table 2 difficult to interpret meaningfully. Specifically, the baselines use different pre-training datasets, which significantly impacts performance, and this is not adequately controlled for. For example, some baselines use PDB-REDO, others AFDB, and Prompt-DDG uses SKEMPI v2.0 directly for unsupervised pre-training. This lack of standardization makes it impossible to isolate the effect of the proposed method from the effect of different pre-training strategies.

2. **Data Leakage Concerns**
   There are serious methodological concerns about potential data leakage in the experimental setup. The authors use Prompt-DDG both as a teacher model and for dataset augmentation, but Prompt-DDG was itself trained on SKEMPIv2.0. This creates a circular dependency where test set information may be leaking into the training process through the augmented data, regardless of splitting schemes. The authors claim to avoid this via the "cross-augmentation" scheme [a technique I'm not aware of, nor was able to find reference for), depicted in Figure 2. However, the explanation of this cross-augmentation is insufficient. The core issue is that even if the augmented data is generated using a Prompt-DDG model trained on a different fold, the model architecture and training objective are the same, leading to similar biases. Thus, the augmented data will still carry information about the test set, even if not directly. The authors need to explicitly address how they prevented this contamination from occurring, particularly given the ablation results that show the outsized impact of the augmentation on performance.

3. **Inadequate Baseline Comparisons for Mutation Search**
   The authors' approach of screening 10,000 random candidates significantly understates the complexity of the protein design problem and ignores established optimization algorithms. Given their efficient ΔΔG predictor as a fitness function, they should have compared against approaches like:
   • CMA-ES (Covariance Matrix Adaptation Evolution Strategy)
   • Gradient-guided Gibbs sampling
   • Basic evolutionary algorithms with standard mutation operators

The strong performance of their random baseline in Table 6 suggests these evolutionary approaches could be quite effective. The current random search baseline does not adequately demonstrate the utility of the proposed method in a realistic protein design scenario.

4. **Overstatement of Framework**
   The authors' claim of developing a "unified framework" for antibody optimization overstates their contribution. What they demonstrate is primarily a successful application of knowledge distillation and data augmentation to improve model efficiency and generalization. While valuable, this falls short of the comprehensive framework they suggest. The integration of Shapley values and mutation search, while interesting, does not constitute a novel framework, but rather a standard application of these techniques with a more efficient predictor.

### Questions
1. Can you provide evidence that all baseline models were trained on equivalent datasets to ensure fair comparison?
2. How specifically did you prevent data leakage given Prompt-DDG's training history on SKEMPIv2.0?
3. Can you provide comparisons against established optimization methods like CMA-ES and gradient-guided sampling?
4. What justifies presenting this as a "unified framework" rather than an efficient implementation of a ΔΔG predictor?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a transformer architecture to predict $\Delta\Delta G$ (the differences in free energy binding due to mutation).  They use knowledge distillation to rather surprisingly obtain a much small, yet more accurate model than the large teach model it is trained on.  They demonstrate that having a light-weight $\Delta\Delta G$ predictor allows them to solve some important downstream tasks involving protein mutation prediction, protein evolution, etc.  There results beat the current state-of-the-art by a significant margin.

### Strengths
This is a strong paper with impressive results.  There should be of interest to people working in learning representation as it shows the effectiveness of using a transformer model to extract knowledge from a much larger model.  The experiments conducted are comprehensive and convincing.  There is a nice ablation study and various real world case studies showing the utility of the predictor.

### Weaknesses
I found the title difficult to comprehend because of the use of $\Delta \Delta G$, which I had no idea about.  Maybe this is common place and just reflects my ignorance, but it slowed down my ability to understand the paper.  This is a very minor comment which I'm happy for the authors to ignore.

I'm also a bit lost why predicting $\Delta \Delta G$ should have such an impact.  Is the binding free energy the overwhelming factor in determining the effectiveness of an antibody?

My intuition would be that predicting $\Delta \Delta G$ would be very difficult as any mutation could cause a significant shape change which is hard to predict.  Thus, I would have thought your predictor would lead to only a moderate improvement.  Clearly my intuition or logic is wrong.  Where am I wrong (or why does your model work so well)?

Why does Light-DDG do so much better than Prompt-DGG given that it is trained using Prompt-DGG?  I know that there are claims that pupils in knowledge-distillation can be better than the teacher, but my experience is that this is rare and for there to be such a large improvement is unusual.  I am assuming that Light-DDG include components not in Prompt-DGG, but I did not pick up what makes the big difference.

### Questions
Why does Light-DDG do so much better than Prompt-DGG given that it is trained using Prompt-DGG?  I know that there are claims that pupils in knowledge-distillation can be better than the teacher, but my experience is that this is rare and for there to be such a large improvement is unusual.  I am assuming that Light-DDG include components not in Prompt-DGG, but I did not pick up what makes the big difference.

I'm also a bit lost why predicting $\Delta \Delta G$ should have such an impact.  Is the binding free energy the overwhelming factor in determining the effectiveness of an antibody?

My intuition would be that predicting $\Delta \Delta G$ would be very difficult as any mutation could cause a significant shape change which is hard to predict.  Thus, I would have thought your predictor would lead to only a moderate improvement.  Clearly my intuition or logic is wrong.  Where am I wrong (or why does your model work so well)?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a simple and effective Light-DDG model to predict the binding free energy change of protein complexes. The method utilizes an augmented large-scale dataset as supervised pretraining and achieves SoTA performance through a simple knowledge distillation strategy. Additionally, a novel mutation explainer is proposed to design Uni-Anti, an antibody optimization framework that enables fast screening with Light-DDG, and the effectiveness of the framework is demonstrated through a case study of SARS-CoV-2.

### Strengths
1. This paper demonstrates the high predictive performance of binding free energy changes using a lightweight transformer-based predictor, enabled by supervised pretraining on a large-scale mutation dataset and knowledge distillation.
2. The authors introduced an iterative Shapley value estimation algorithm, a coarse-to-fine iterative approach that effectively identifies key mutation sites, replacing the traditional Shapley value algorithm.
3. The Uni-Anti framework enables rapid antibody optimization through fast screening without requiring a generative model, offering a practical solution for antibody design.

### Weaknesses
1. The backbone lightweight Transformer processes E(3)-invariant features, but the paper does not discuss whether the model guarantees E(3)-invariant outputs. Specifically, while the *input* features are invariant to rotations and translations, it's not clear if the *output* of the transformer maintains this invariance. The architecture itself, without specific constraints or design choices, does not inherently guarantee E(3) invariance of the output, which is crucial for the physical consistency of the predicted binding free energy changes.
2. Although the iterative Shapley value estimation algorithm is proposed to efficiently explore a large mutation space, it may lack a mathematical guarantee of accurately approximating Shapley values. The algorithm's convergence properties and error bounds are not established, making it difficult to assess the reliability of the identified key mutation sites. Without a formal analysis, it is unclear how well the iterative approach approximates the true Shapley values, especially in complex mutation landscapes. The heuristic nature of the algorithm raises concerns about its robustness and generalizability.

### Questions
1.	Could you clarify how the mutated structures (Mutant Str.) of Light-DDG in Table 4 are provided?
2.	While Prompt-DDG is a SoTA model, there may be potential for inaccuracies in pseudo-labeling. If so, would any methods be considered to address these?
3.	Additionally, since augmentation could produce samples highly similar to SKEMPI v2.0, is there a filtering step in place to prevent overlaps? If not, would this be a consideration?
4.	The dWJS [1] might apply to the antibody optimization task. Would a comparative analysis be possible?
5.	The reference to the SAbDab dataset on p9 may be incorrect. Could you please verify?

[1] Frey et al. (2024) "Protein Discovery with Discrete Walk-Jump Sampling", ICLR

### Soundness
3

### Presentation
4

### Contribution
3

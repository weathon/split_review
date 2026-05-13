# Non-Parametric State-Space Models Over Datapoints and Sequence Alignments

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Non-parametric models are flexible and can leverage a context set to express rich mappings from inputs to outputs. However, these methods often scale super-linearly in context size, e.g., attention-based
methods scale quadratically in the number of data points, which in turn limits model expressivity.  In this work, we leverage advances in state-space modeling and introduce Non-Parametric State
 Space Models (NPSSM). We find that NPSSMs attain similar performance to existing non-parametric attention-based models while scaling linearly in the number of datapoints. We apply NPSSMs to the task of genotype imputation, where the linear scaling enables larger context sets resulting in competitive performance relative to other methods and widely used industry-standard tools. We also demonstrate the effectiveness of
NPSSMs in the context of meta-learning where the ability to efficiently scale to larger training sets provides more favorable compute-to-accuracy tradeoffs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce the non-parametric state space model (NPSSM), which scales linearly with the number of data point unlike other attention-based models. The proposed approaches is applied in the context of genotype imputation and meta learning.

### Strengths
The proposed approach is simple and inherits the linear scaling of state space models such as BiMamba.

### Weaknesses
The methodological component of the paper reads excessively like a pure application (without methodological novelty). First the model basically applies BiMamba twice without further modification. Second, a big  emphasis of the proposed approach is its linear scaling, however, this is not discussed or analyzed in the methods, basically, because it translates directly from BiMamba.

The first experiment (protein analysis) is underwhelming. First they show that increasing k does not improve the performance of neither of the approaches considering, thus defeating the need of a more expressive, but more expensive, model. Second, the model considered had 1M parameters vs. 3.5M in Notin et al. (2023b). Why not consider the larger model at least for NPSSM? Also, from Table 1, it doe not look like PNPT scales (in memory) much worse than NPSSM? One would expect the factor (~2) not to remain that similar for K=1000 and K=1500.

The second experiment is not very convincing because the advantage of NPSSM over MSA Transformer is not clear. This because i) results (Tables 2 and 3) are only presented on a single dataset, ii) the variability and dependency of the main performance characteristics on hyperparameter choices is not clear (though explored via ablation), and iii) computational cost is briefly illustrated in Figure 5. However, is is not clear which context size is used for the main experiments in Tables 2 and 3 and why given the relationship between context size and performance (in Figure 2), the proposed model is not more much better than MSA Transformer in terms of r2.

From Table 3 and Figure 2 it is not clear how the MSA Transformer can reach a r2=0.956 when it runs out of memory before reaching r2=0.95 in Figure 2?

Why not considering the experiment in Table 6, but starting from the best model in Table 3? Note also that the value of k used in the main experiments is not noted.

### Questions
From Table 3 and Figure 2 it is not clear how the MSA Transformer can reach a r2=0.956 when it runs out of memory before reaching r2=0.95 in Figure 2?

Why not considering the experiment in Table 6, but starting from the best model in Table 3? Note also that the value of k used in the main experiments is not noted.

### Soundness
2

### Presentation
1

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
1. The paper introduces NPSSM, which adapts state-space models (SSMs) into a non-parametric model for  genotype imputation and protein mutation prediction tasks.
2. NPSSM replaces attention with bidirectional Mamba-based SSM layers which achieves a linear complexity in reference set size, an advantage over Transformers which scale quadratically.
3. NPSSM demonstrates competitive performance with transformer-based models

### Strengths
1. The paper is well written.
2. NPSSM achieves competitive performance against SOTA transformer model.
3. Memory usage is low due to the use of SSMs, a known benefit that allows for efficient handling of large datasets and contexts.

### Weaknesses
 **Limited Novelty**: The primary contribution appears to be the replacement of transformers with SSMs, gaining known benefits like linear scalability, handling of long-range dependencies through selectivity. However, these advantages largely derive from established SSM properties rather than novel methodological improvements.

**Ablating the use of Attribute-Specific Components**: The introduced attribute and data-specific SSM layers may benefit from ablation studies. For instance, it is unclear how much of the heavy-lifting is done by the two components and can we remove one of them. Should the order of SSM application be Attribute and then Data or vice versa. Can we instead flatten the sequence.

**Possibly Insufficient Evaluation**: The model is tested on a limited set of baselines. I am not an expert in these tasks but I feel that expanding the number of tasks and baseline models would strengthen the claims of generalizability.

### Questions
N/A please see weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes an SSM approach to non-parameteric learning. i.e., the setting where the dataset itself is used as input to the model, rather than learning a model based on the training data and then discarding the data. This setting is particularly advantageous for meta-learning where one seeks a model for new datasets. 
In previous work, transformers have been proposed for this task (e.g., MSA transformer and NP transformers, mentioned in the paper). The current paper proposes to instead use state space models for this, motivated by their ability to handle longer contexts with less memory requirements.
On the one hand, the idea is reasonable, and the empirical results confirm that performance is competitive and does allow use of longer contexts. On the other hand, it seems like the novel component here is mostly replacing transformers with SSM, but the other conceptual aspects of using it for meta-learning (e.g., various masking losses) have been introduced in the previous NP transformer works.

### Strengths
As mentioned above, it is good to see that the advantages of SSM are also manifested in this setting.

### Weaknesses
It seems like conceptually the approach largely follows that of NP transformers, and thus the main contribution is to show that state space models are a viable alternative in this case. If the main claim is empirical, I would expect more extensive experiments and clearer gains. The current experiments do not sufficiently demonstrate the advantages of the proposed method over existing approaches, particularly given the computational overhead of SSMs. The performance differences between the proposed method and HMMs are not statistically significant, and it is unclear why the proposed method should be preferred given the added complexity. The ablation study is also limited, and it is not clear how the different components of the model contribute to the overall performance. Specifically, the ablation study does not explore the impact of different masking strategies or the effect of varying the size of the input context. Furthermore, the comparison to the flattened input is not a strong baseline, as it does not account for the sequential nature of the data. The lack of a direct comparison to a similarly trained SSM on the target dataset is also a significant omission. The paper would benefit from a more thorough analysis of the model's performance and a more comprehensive comparison to existing methods.

### Questions
1. For Table 3, was the HMM trained on chromosome 20?
2. Typo: “Each these methods “ -> “Each of these methods “
3. HMMs seem to have similar performance to the non-parameteric methods in Table 2 (differences seem small and not statistically significant unless you show otherwise).. Can you comment on why HMM is an inferior solution in this case?
4. Another natural baseline, which I don't see but maybe I missed, is to just train on the target dataset D_C, with an SSM model (but still perform some pre-training with masking).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors apply SSMs, an efficient sequence modeling technique, to non-parametric transformers. The experiments validate that the Non-Parametric State Space Models (NPSSM) attain similar performance to exising attention-based methods.

### Strengths
- The method is well-motivated. Given that current non-parametric models typically rely on the self-attention mechanism, replacing attention with SSMs is a reasonable approach.
- This submission validates the effectiveness of SSMs in modeling, contributing to a better understanding of SSMs in the field.

### Weaknesses
 - (**major**) The paper includes an acknowledgment section, at the end of the submission, which potentially reveals author information and violates the double-blind review policy.
- Since SSM can be viewed as an efficient sequential modeling technique, the authors should compare their method with other efficient attention algorithms, including linear attention works.
- It should help if authors provide a formal formulation of \mathcal{L}_{MLM} and \mathcal{L}_{Aux}. I'm still a little confused about the method pipeline.

### Questions
Can this approach be applied to other tasks, such as language tasks?

### Soundness
4

### Presentation
3

### Contribution
3

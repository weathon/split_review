# Simplified Mamba with Disentangled Dependency Encoding for Long-Term Time Series Forecasting

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 3, 6

## Abstract
Recent advances in deep learning have led to the development of numerous models for Long-term Time Series Forecasting (LTSF). However, most approaches still struggle to comprehensively capture reliable and informative dependencies inherent in time series data. In this paper, we identify and formally define three critical dependencies essential for improving forecasting accuracy: the order dependency and semantic dependency in the time dimension as well as cross-variate dependency in the variate dimension. Despite their significance, these dependencies are rarely considered holistically in existing models. Moreover, improper handling of these dependencies can introduce harmful noise that significantly impairs forecasting performance. To address these challenges, we explore the potential of Mamba for LTSF, highlighting its three key advantages to capture three dependencies, respectively. We further empirically observe that nonlinear activation functions used in vanilla Mamba are redundant for semantically sparse time series data. Therefore, we propose \model, a Simplified Mamba with disentangled dependency encoding. Specifically, we first eliminate the nonlinearity of vanilla Mamba to make it more suitable for LTSF. Along this line, we propose a disentangled dependency encoding strategy to endow Mamba with efficient cross-variate dependency modeling capability while minimizing the interference between time and variate dimensions. We also provide rigorous theory as a justification for our design. Extensive experiments on nine real-world datasets demonstrate the effectiveness of \model over state-of-the-art forecasting models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the adaptation of a recently emerged  Mamba architecture to long-term time-series forecasting. It highlights three key aspects: order, semantic, and cross-variate dependencies. The derived Samba architecture encompasses two branches for temporal and variable dependency encoding, of which the encoded representations are concatenated to produce forecasts.

### Strengths
It is interesting to investigate the pros and cons of the Mamba architecture, or more broadly, structured state-space models (SSMs), on long-term time-series forecasting.

### Weaknesses
Concerns Regarding the Soundness and Contributions of the Paper

1. Overlooking the Unique Advantage of Mamba: Modeling Long Sequences

Mamba, a recent and popular instantiation of state-space models (SSMs), is renowned for its efficiency in processing long sequences. It significantly reduces the computational overheads of self-attention in Transformers while seemingly maintaining long-term dependencies in various real-world datasets. However, this paper primarily compares time-series representation learning among MLP, Transformer, and Mamba, fixing the lookback length at T=96. When modeling relatively shorter sequences, the necessity of introducing SSMs diminishes significantly, which in turn reduces the impact of this research. The core advantage of Mamba, its ability to handle very long sequences efficiently, is not leveraged or explored in the experiments, thus missing a key opportunity to demonstrate its potential in time-series forecasting.

2. Inappropriate and Biased Expressions/Claims

Lines 014-016: The claim, "However, most approaches still struggle to comprehensively capture reliable and informative dependencies inherent in time series data," lacks rigor. Existing time-series forecasting models have made significant progress in learning effective time-series representations and deliver commendable forecasts in many scenarios. The paper's experiments do not show a substantial difference in model performance to support this claim. The statement is too broad and does not acknowledge the progress made in the field.

Lines 052-054: The assertion that "they struggle with perceiving temporal order due to the permutation-invariant nature of self-attention, even with positional encodings," is debatable. It is not clear how sensitivity to sequence order impacts the capability of learning effective temporal representations. Extensive research on position encoding for Transformers has already led to the success of modern large language models. The experiments in Table 1 only demonstrate that Transformers are less sensitive to order permutation than Linear and Mamba, which is expected. However, it is unclear how this capability affects temporal representation learning. In fact, being less sensitive to order permutation might be advantageous in sequence modeling. Furthermore, the use of Mamba to model cross-variate dependency seems flawed, as time-series variates lack a ground-truth order. Following the author's logic, using an order-sensitive model like Mamba for cross-variate dependency might not be appropriate. The paper does not provide a clear justification for why order sensitivity is crucial for time series forecasting, especially given the success of order-agnostic models.

Lines 058-061: The statement, "existing approaches that utilize cross-variate dependency (Channel Dependent, CD) frequently underperform compared to methods that treat each variate independently (Channel-Independent, CI)," is not universally applicable. The performance of CD and CI approaches highly depends on specific cases. Studies, such as iTransformer, have demonstrated the benefits of cross-variate modeling. The claim is overly general and does not consider the nuanced performance of different models under various conditions.

3. Insufficient Experiments Leading to Unreliable Conclusions

The analyses in Section 4, which inform the design of Samba, are primarily based on experiments conducted on the small ETTm1 dataset and compared across basic neural architectures like Linear, vanilla MLP, and Transformer. These results can be interpreted in multiple ways, not solely as the authors suggest. For instance, Table 1 shows Transformers' reduced sensitivity to order perturbation, which may actually be beneficial for encoding effective temporal representations. Table 2 investigates patching effectiveness, originally introduced in PatchTST, yet PatchTST itself is not included in the analysis. Additionally, the impact of patch size on results and whether all datasets lead to the same conclusion are unexplored. Other factors, such as TSMixer extending MLP-based architectures on time-series and PatchTST's designs to prevent overfitting, are not considered in Table 3. Consequently, the analyses in Section 4 are unconvincing regarding the necessity of introducing Mamba. The experimental scope is too narrow to draw strong conclusions about the general applicability of Mamba for time-series forecasting.

4. Seemingly Downgraded Performance of Baselines

For example, in Table 4, PatchTST on ETTh1 produces an MSE of 0.469 and an MAE of 0.454. However, the original paper reported much lower errors (https://arxiv.org/pdf/2211.14730).

5. Lack of Unique Contributions

In addition to studying Mamba for time series, this paper appears to offer few unique contributions or novel insights. Concepts such as patching, cross-variate and cross-time dependency, and normalization to prevent overfitting have been extensively explored in prior research. Furthermore, Transformer variants in time series have effectively addressed challenges in these areas. Therefore, without the focus on modeling very long sequences, the necessity of adapting Mamba for time series remains questionable.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper:

1. Identifies three types of dependencies in multivariate time series data. 
2. Simplifies the Mamba activation functions to eliminate non-linearity. 
3. Proposes a dependency encoding strategy to disentangle these dependencies, minimizing interference between the time and variate dimensions.

### Strengths
1. The authors provide a clear and comprehensive description of the key dependencies in LTSF modeling, including order dependency, semantic dependency, and cross-variate dependency. The model architecture is well-designed to capture these dependencies.

2. The architecture introduced in this paper to capture relationships across both temporal and variate dimensions enhances Mamba's ability to effectively model cross-variate relationships.

3. The experiments conducted demonstrate that the proposed architecture outperforms previous methods and can be effectively transferred to other models.

### Weaknesses
 1. The paper contains several spelling and formatting errors. The authors should carefully check them before submission. Examples include: 
   a) Inconsistent abbreviations, with “LTSF” sometimes written as “LTST”; 
   b) Formatting issues in Theorem 1; 
   c) Various spelling errors.

2. The title and model name "Simplified Mamba, SAMBA" emphasize a simplification of Mamba, specifically through the removal of non-linearity. However, according to the paper, the performance improvements from this regularization method are not particularly significant compared to other strategies, such as patch tokenization. Additionally, the authors mention that the elimination is not fully implemented, as non-linear activation function remains in the gating mechanism. Furthermore, the overall SAMBA architecture actually employs Mamba along the temporal dimension and bidirectional Mamba along the variate dimension, making it more complex rather than simplified, compared to the original Mamba for sequence modeling. Thus, the authors might consider rebranding their methods to avoid misleading readers.



### Questions
1. About order dependency:

The statement and evidences to prove that Transformer-based models are unsuitable for modeling order information seems insufficient. 

First, improving a model's perception of order information can depend on two factors: the tokenization and the training method. In tokenization, if different lag timesteps are treated as distinct features inside a token (e.g., series embedding as in Linear models and iTransformer, or patch embedding as in PatchTST), shuffling values across timesteps will clearly impact performance, as the linear projection layer automatically considers them as separate input features. However, if timestep values are projected into the same latent space during tokenization, the model must rely on additional structures (such as attention + positional encoding) to learn this order information. Can this order be learned with pure Transformers? The success of LLMs proves that models can learn precise positional information. LLMs accurately identify and utilize context positions for next-token prediction without making sequencing errors, thanks to the learning of mechanisms like induction heads, which has been widely validated. Autoregressive training method enforces models to learn these temporal ordering algorithms.

The choice of tokenization and training method is largely independent of the model architecture. Both Transformers and Mamba can use these methods to improve the capture of positional information in LTSF tasks. Experimental results in the paper also show that patch tokenization enhances performance across different architectures. It separates timesteps within a local period into distinct features inside a token, rather than treating all timesteps as equivalent tokens in the attention mechanism.

Constructing algorithms between tokens in attention (or SSM in Mamba) involves learning the sequence's semantic information. The richer the semantic information, the more we need to model algorithms at a finer granularity (shorter patch sizes). The paper suggests that patching enhances semantic dependency learning, but this seems contradictory. Patching likely reduces the need for complex semantic relationship modeling, functioning as a form of attention regularization that improves performance on datasets with simpler semantics, contrary to Assumption 2. Correspondingly, Linear models treat the entire series as embeddings and all timesteps as lag features, omitting the need to construct semantic relationships between timesteps, which aligns with the statement in the paper. However, the analysis of patching seems inconsistent. The authors could experiment on datasets with richer semantic information (e.g., ODE-based datasets with underlying dynamics) to see if pure timestep embedding outperforms patch embedding.

In summary, does Mamba have an advantage over Transformer-based models in modeling order information as claimed? It seems so, but this advantage may come from patching tokenization and possibly from Mamba's SSM handling of sequential/causal token information. Previous LTSF encoder-only Transformers may lack the sequential structure. The authors could compare Mamba to Transformers using causal masks/training methods to further establish Mamba's structural superiority in LTSF. Additionally, more discussion is needed to support the definitions and statements of semantic dependency.


2. About the dataset selection：

The experiments in Tables 1-3 and Figure 1 are conducted solely on the ETTm1 dataset, which seems insufficient to draw general conclusions. The nature of the datasets significantly impacts the performance of different models with varying degrees of regularization.

The performance comparison in Table 1 using shuffling on a single dataset appears insufficient (actually, I hold a similar view regarding these experiments conducted in the DLinear paper). Here's a simple counterexample: 

Consider an invertible MA(1) process, $ X_t = \mu + \varepsilon_t + \theta \varepsilon_{t-1} $, with two sub-optimal predictors: one using the global average of the input and the other using the last value as the prediction. It can be shown that the first predictor is better or equal to the second one under invertible condition. However, if the input is shuffled, the first predictor’s performance does not deteriorate, while the second, less optimal predictor's MSE decreases when $ \theta > 0 $, remains unchanged at $ \theta = 0 $, and increases when $ \theta < 0 $. This indicates that comparing performance drops due to shuffling may not be sufficient to prove a model’s sensitivity to order, as better models may also learn predictors insensitive to position.

The conclusions from Table 2 may also be dataset-sensitive. For datasets with underlying dynamics and shifting multivariate effects, exposing more temporal tokens for algorithm construction in attentions could be more advantageous. The authors could extend experiments to datasets like Solar and Exchange to strengthen these claims.

Table 3 should be a foundational point of the paper, but it requires validation across more datasets. The choice between model linearity and complexity largely depends on the dataset. When clear non-linear relationships exist, the model may need to build more complex algorithms between temporal tokens, leading to different conclusions.

Figure 1 shows that removing activation functions increases the model’s regularization. The authors could consider testing this on more complex datasets, such as Traffic (or maybe PEMS?), to confirm that stronger regularization is indeed beneficial.


### Conclusion

Even though I have some concerns about the authors’ claims and experimental methods, the authors have put in a substantial amount of work throughout the paper. Therefore, I look forward to further discussion with the authors on these points before giving a final score.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a simplified Mamba with disentangled dependency encoding for long-term time series forecasting, in which the nonlinearities in vanilla Mamba are removed to improve the generalization ability of the framework and a theoretically sound disentangled encoding strategy is introduced to separate the cross-time and cross-variate dependencies. Experiments demonstrate the effectiveness of the proposed framework.

### Strengths
1.The organization of this paper is clear.

2.The definition of three critical dependencies in time series data is novel and interesting.

### Weaknesses
1.This paper lacks innovation, as the authors only model interactions along time dimension and variate dimension separately, without the targeted design towards disentangled dependency encoding strategy. The authors should provide a detailed description towards their disentangled dependency encoding strategy. Specifically, the paper does not articulate how the proposed architecture ensures the disentanglement of cross-time and cross-variate dependencies. The authors should clarify the mechanisms that prevent these dependencies from interfering with each other during the encoding process. Furthermore, the paper lacks a clear definition of what constitutes a 'disentangled' representation in the context of time series data, which makes it difficult to evaluate the effectiveness of the proposed approach.

2.The design of the SAMBA block is also similar to existing works [1, 2]. It seems that the only difference between this work and existing work is the removal of the nonlinear activation function between the Conv1D and SSM layers. Although the authors claim that this approach can mitigate the overfitting issue, Table 3 shows that for the Path+Mamba method, removing the nonlinear activation function actually results in a performance drop. The authors should provide a theoretical analysis about removing the nonlinear activation function can mitigate the overfitting issue and validate their claim on additional datasets (e.g., ECL, Traffic, and Weather datasets). The paper should also address why the removal of the nonlinear activation function does not consistently improve performance across all model variants and datasets. The inconsistent results raise questions about the general applicability of this design choice.

3.The paper has some weaknesses in the experiments, which are not convincing enough:

(1)The authors claim that they implement the baseline results by using the TimesNet Github repository in Section B.1. However, they also claim that the full results of predictions come from iTransformer in Section B.2, which is confusing. It would be helpful to have an explanation for these differences. It is unclear why the results are not consistently derived from a single source, which raises concerns about the comparability of the experiments. The authors should clarify the specific implementation details for each baseline and justify the use of different sources.

(2) Some tables lack sufficient explanation, making them difficult to understand. For example, in Table 1, what do the bold results mean? Does the transformer refer to the ordinary transformer framework or a state-of-the-art (SOTA) transformer-based framework (e.g., iTransformer)? In addition, in Table 3, why is there no comparison with the Patch+MLP method? The authors should provide a detailed explanation of the notations and abbreviations used in the Tables. In addition, the authors should include comparative experiments with the SOTA transformer-based framework and the Patch+MLP method in Table 1 and Table 3, respectively. The lack of clarity in the tables makes it difficult to interpret the results and assess the effectiveness of the proposed method.

(3) Although the authors add the efficiency comparison between SAMBA and the baseline models, there is no clarification on which dataset(s) the comparison is conducted. In addition, the term 'Mem' in the efficiency comparison is not explained, which makes the experiments regarding efficiency comparison confusing. Please specify which dataset(s) are used for the efficiency comparison, and provide an explanation for the 'Mem' metric used for the efficiency comparison. The absence of these details makes it difficult to verify the efficiency claims and understand the practical implications of the proposed method.

4. There are many typos and writing mistakes in the manuscript. For example, on page 22, “Solar-Energy)or” should be "Solar-Energy) or" and "Exchange ) overall" should be "Exchange) overall". The manuscript requires thorough proofreading.

### Questions
See Weaknesses.

### Soundness
2

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
5

### Summary
This paper proposes a Mamba-based structure to capture three sources of information from multivariate time series data: order dependency, semantic dependency and cross-variate dependency, and optimizes the Mamba structure by removing nonlinearities and incorporating a theoretically sound disentangled encoding strategy that appropriately integrates cross-variate dependency to the model, enhancing the model’s global representation and predictive capabilities. Experiments on multiple datasets conforms the efficacy of SAMBA structure.

### Strengths
The overall idea of applying Mamba for MTSF is novel, and the introduction of 'semantic dependency' is novel to the field of time series. Moreover, theroretical properties of the method are also provided.

### Weaknesses
The introduction of Mamba structure and its advantages compared with Transformer structure in MTSF should be in more details. 

The explanation of  semantic dependency is not quite informative, and the boundary between order (temporal) dependency and semantic dependency seems unclear. Moreover, I wonder why the semantic dependency here does not include historical values from other covariates. 

Moreover, there are many LLM-based methods for MTSF in recent years, and is highly recommended to be included in literature / benchmark methods such as LLM4TS, GPT4TS, CATS etc. I will happily raise my score if these concerns are addressed.

### Questions
I have several comments regarding the methodology details:
1. Is the model performance highly dependent on the parameters of patching?
2. The structure of SAMBA block should be directly compared with MAMBA in Fig 3 to show the difference. 
3. How does SAMBA blocks achieve disentanglement encoding successully separate cross-time and cross-variate dependencies? It seems to me that such entanglements still exist through sum and back propagation.

### Soundness
3

### Presentation
3

### Contribution
3

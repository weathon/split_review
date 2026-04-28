# Boosting Recovery in Transformer-Based Symbolic Regression

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
The traditional objective in regression is generalization. That is, learning a function from training data that performs well beyond the training data. Symbolic regression adds another objective, namely, interpretability of the regressor.  
In the context of regression, interpretability means that the representation of the regressor facilitates insights into mechanisms that underlie the functional dependence. State-of-the-art symbolic regressors provide such insights. However, the state of the art predominantly incurs high costs at inference time. The recently proposed transformer-based end-to-end approach is orders of magnitude faster at inference time. 
It does, however, not achieve state-of-the-art performance in terms of interpretability, which is typically measured by the ability to recover ground truth formulas from samples. Here, we show that the recovery performance of the end-to-end approach can be boosted by carefully selecting the training data. We construct a synthetic dataset from first principles and demonstrate that the capacity to recover ground truth formulas is proportional to the available computational resources.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to improve the recovery performance of transformer-based symbolic regression methods through more systematic training data generation. The authors represent equations as register machine programs (RMPs) and propose finding minimal RMPs with standardized input/output variables. The approach shows improved recovery rates on simpler equations from benchmarks like Feynman equations while maintaining the fast inference advantage of transformer-based approaches.

### Strengths
- Addresses an important limitation in transformer-based symbolic regression methods by focusing on their poor recovery performance
- The proposed minimal RMP generation approach shows promise in reducing expression complexity
- Demonstrates meaningful improvement in recovery rate over E2E methods for simpler Feynman problems while maintaining fast inference times

### Weaknesses
 - Limited evaluation on complex problems - the approach's effectiveness seems primarily demonstrated on simpler equations
- The standardization approach, while helpful for training, may limit the model's ability to handle complex nonlinear relations with varying constant ranges
- The empirical advantages over E2E approach are not clearly demonstrated through comprehensive metrics (e.g., R² accuracy, black-box problems), especially given that E2E's data generation could potentially be adjusted to achieve similar results
- The claim that RMPs provide a more succinct representation than expression trees is not universally true; in many cases, RMPs can require more tokens due to their register-based nature.
- The constant range used for training is limited, potentially hindering generalization to real-world problems where constants can vary widely. The use of a single scalar for scaling all input features is also a limitation, as real-world data often requires different scaling factors per dimension.
- The observed performance drop with increasing context length contradicts findings in previous works and general trends in machine learning, where more data typically improves performance. This suggests a potential issue with the model's ability to leverage additional input-output pairs.

### Questions
* Do minimal RMPs have equivalent expression trees? Can you comment on potential performance if the model was trained on expression tree versions of the same minimal RMP datasets?

* Figure 4 presents recovery rate results. Could you provide:
   - R² accuracy performance on SRBench problems (both ground truth and black-box functions)
   - Fitting accuracy (R²) comparison across different dimensions relative to E2E

* In Figure 5, why does recovery performance drop with context length? Shouldn't more observations improve the performance?

* Given that data generation includes RMP enumeration for finding minimal RMPs, how time-consuming is the data generation process?

* You report that in 10K equations, E2E contains around 6.4K equivalence groups, and E2E prioritizes fast data generation. Could E2E generate the same number of equivalent groups given equal time?

* One drawback of E2E data noted in the paper is its tendency toward complex forms, especially compared to low-dimensional Feynman equations. However, E2E's data generation can be controlled through hyperparameters (minimum/maximum number of unary and binary operators). Have you explored if reducing equation length in E2E could lead to simpler equations and better recovery, even if it comes at the cost of lower accuracy?

* Would it be possible for the authors to share the code for data generation and model weights?

* Could you explain:
   - Why mRMPs per dimension decreases from D=3 to D=5 in Appendix Figure 3?
   - Is the constant range [-10, 10] reasonable for practical problems, given E2E uses [-100, 100]? Can the model generalize to out-of-range constants?
   - Could you provide examples of the 17% of recovered formulas that result from generalization (Lines 409-412)?
   - What does "implicitly" vs "explicitly" mean in Lines 077-079?
   - In Line 200-203, why is c₃ ∈ ℝ? Shouldn't it be c₃ ∈ ℝᴰ?

[Note: There appears to be a typo in Line 285 where "RPM" should be "RMP"]

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
The paper proposes a a structured way to  select the training data and construct a synthetic dataset from first principles, improving the interpretability and efficiency of symbolic regression using transformer models.

### Strengths
1. The article is clearly written and its structure is well-organized

2. The experimental validation in the article is sufficient.

3. The method proposed in the article is practical and demonstrates good effectiveness and innovation.
    What’s most valuable is that the method integrates well with the hardware.

### Weaknesses
The paper highlights the transformer model’s tendency to memorize training data, as 51% of the recovered formulas are from the training set. This method is somewhat too direct, which may lead to overfitting of the model. The direct mapping from training data to recovered formulas, while efficient, raises concerns about the model's ability to generalize to unseen data. The high percentage of memorized formulas suggests that the model might be learning specific training examples rather than underlying mathematical relationships. This could limit the practical applicability of the model in scenarios where the target formulas are not well-represented in the training set. Furthermore, the paper does not provide a detailed analysis of the types of formulas that are memorized versus those that are genuinely learned, which would be valuable for understanding the model's limitations.

### Questions
How does this method achieve fine-grained control of registers to complete a series of complex computational tasks?

### Soundness
3

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
This paper addresses the recovery performance limitation in transformer symbolic regression models by introducing a novel data generation approach using register machine programs (RMPs). After pre-training previous transformer SR models with the same architecture on this new data, the authors demonstrate significant improvement in recovery rates while maintaining fast inference times.

### Strengths
* Addresses a valid and current challenge in transformer-based symbolic regression methods
* Takes a novel approach by focusing on data generation improvements
* Shows great results in the improvement of recovery rates from the new data generation setting

### Weaknesses
 **Major Concerns:**

*   Overlook of literature: For example, [1] is the pioneering work in transformer SR which also similarly follows skeleton-based training (having placeholder parameter for constants in symbolic expressions).

*   While the paper focuses on recovery rate as the interpretability metric, evaluation on semantic symbolic correctness metrics such as out-of-domain generalization and extrapolation would also be helpful as they are more flexible than recovery rate and can consider other possibilities such as mathematical approximations or equivalence.

*   The paper's approach of normalizing outputs in addition to inputs may fundamentally alter the underlying function behavior and the mapping to the corresponding symbolic function. For example, If we normalize the output, the functions with same skeleton but different constant values may collapse which might lead to negligible impact of some symbolic terms. I do think that normalization might help transformer to have better memorization mostly for simple problems like Feynman. How do authors make sure that the correspondence between symbolic expressions and data observations are following original data behavior after normalization, particularly for more complex expressions?

*   The main novelty is in data generation for transformer SR model training, specifically the representation of expressions as register machine programs (RMPs). Not enough evidence is provided justifying RMP over expressions as sequence (prefix notation). Additional experiments are needed:
    1. Ablation for performance with different data generation components
    2. Comparison with [1] which also generates expression skeletons with placeholder parameters. [1] has shown a better recovery rate than (kamienny et al., 2022) due to its simpler data generation setting and focus on lower-dimensional problems. I would be interested to see the comparison of your method with [1] on Feynman problems with d_max = 3.


*   Concern on the reported results in Figure 4:
    1. I don't understand why robustness to noise improves this much compared to other baselines. There's no detail from authors about adding noise to the new training data. Why this happen?

    2. Limited comparison with recent SR models like uDSR [2], TPSR [3] and PySR [4]

*   It's not clear what are the main features in new data generation setting that lead to this recovery boost? Ablation analysis is needed on the data generation components. For example, RPM vs expression prefix notation, target scaling, RMP verification steps, etc.


**Minor Comments:**
*   Introduction writing cold be improved. There should be more focus on the contributions of the work than motivation or examples for symbolic regression. Figures 1-2 could move to appendix.

*   What beam size / inference sampling size were used for E2E and E2E-RMP results?

### Questions
provided above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a new generation method for end to end symbolic regression with transformers, replacing the tree representation commonly used to sample functions by Register Machine Programs (RMP), a representation equivalent to the directed acyclic graphs that appear when one removes common subexpressions in trees. 

A training set is generated by enumerating all RMP for a given input dimension, up to a small number of instructions (ie operations). Then, the model proposed in Kamienny et al. (2022) is trained on this dataset, and tested on two small external test sets: Feynmann and Strogatz, for a total of 130 examples. 

On this test set, the authors observe that the recovery rate of their new models is better than previous end to end transformer-based approaches.

### Strengths
The idea of adapting the training set of symbolic regression models, by selecting "more desirable", simpler, functions, is promising.

### Weaknesses
Novelty is extremely limited. The paper uses the architectures and generation techniques from D'Ascoli 2022 and Kamienny 2022, and the constant estimation methods from Biggio 2021. The main new element is the introduction of RMP, but its advantage over the expression trees used in previous works is not clear.

In previous works, expression trees are randomly generated, and a random tree usually has no common subexpressions (i.e. the corresponding DAG is the tree). As a result, the RMP introduces in this paper are most of the time equivalent to the trees they are supposed to replace. Besides, the RMP seems to result in longer sequences than enumerated trees. For instance, the expression $-sin(x_0)+0.3sin(x_0-x_1)$, given as an example in section 3.1, can be represented as a tree with no common subexpressions, and tokenized as 10 tokens. The corresponding RMP uses 31 tokens. What is the benefit?

The paper is difficult to read, it contains a number of incorrect and controversial statements (see below and questions), and does not clearly describe the generation techniques used, and the architecture ablation performed.  For example, figure 4 suggests data generation includes noise, this is not mentioned in sections 2.2 and 2.4. Section 3.1 describes the architecture used as an encoder-decoder model (as Kamienny), but line 332 states "Therefore, a training example with 192, 448, and 960 data points and 64 RMP tokens results in total context sizes of 256, 512, and 1024, respectively." which evokes a decoder-only (GPT-like) architecture, where input and output are concatenated. This notion of "context length" is repeated in the ablations. 

The evaluation is very limited. The model is evaluated on 130 examples only. Figure 5 suggests that model performance (recovery) on its train and test set is around 15%, but it is 40% on the Feynman dataset. This may be due to the fact the most functions in the Feynman set are extremely simple. Besides the authors acknowledge that more than half of the Feynman test functions are already in the train set. This data contamination weakens the claims made in the paper.

### Questions
* l.123 The random sampling method for expression trees was introduced in Lample & Charton 2020 (Deep learning for symbolic mathematics)
* l.147 Kamienny 2022 clearly shows the benefit of estimating constants at inference, and fine-tuning them using BFGS, over predicting a "skeleton" with a special token replacing the constant. You seem to be using the latter, why?
* l. 191 Charton 2021 is not about symbolic regression, maybe cite D'Ascoli 2023 instead, who observe the overfitting
* l. 310 the three token representation for floats was introduced in Charton 2021
* l. 324: "As usual, this number is rounded to the next power of two, which here is 64." why round the output sequence length to a power of two in an encoder-decoder architecture? 
* l. 330  "The RMP tokens are embedded into demb-dimensional space using a standard embedding layer. The
embeddings are then fed into a standard transformer decoder stack." Are you feeding the desired output as output of the decoder? This is not clear.
* l. 333 "total context sizes of 256, 512, and 1024, respectively": context size makes no sense in a decoder-only architecture
* l. 339  "Models are trained until the loss on the validation set is saturated." Can you explain what you mean by "saturated loss"?
* l. 347 the R2 score certainly predates La Cava, it is usually attributed to Pearson.

### Soundness
2

### Presentation
1

### Contribution
2

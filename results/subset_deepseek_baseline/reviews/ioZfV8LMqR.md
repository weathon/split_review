## Summary

The paper introduces a new few-shot design optimization setting where evaluating a design yields both a scalar performance metric and high-dimensional auxiliary information (e.g., sensor time series). A history of related tasks is available for training. The authors propose a transformer-based neural surrogate model that predicts performance from a small context of evaluated designs by exploiting the auxiliary information. They create a large-scale gripper design benchmark with tactile feedback (4.28M designs across ~1K objects) and demonstrate that their method significantly outperforms a baseline using only reward information in both few-shot prediction and Bayesian optimization of unseen tasks.

## Strengths

- **Practical and well-motivated problem setting**: many real-world optimization problems (robotics, drug discovery, hardware design) produce rich auxiliary information beyond a scalar reward, and leveraging this information across tasks is a natural and important extension of the standard black-box setting.
- **Large-scale benchmark contribution**: the gripper design task with tactile feedback is substantial (thousands of objects, millions of designs) and will be valuable for future research on few-shot design optimization with auxiliary information.
- **Clear experimental methodology**: the authors control for parameter count by including an f-only(+) baseline with more parameters, confirming that the performance gain comes from using auxiliary information rather than model capacity. They also include a nearest-neighbor baseline to rule out trivial reasoning.
- **Clean improvement in both prediction and optimization**: the model consistently achieves lower MSE across all context sizes, especially at small context sizes (improvement of ~15% at context 5), and translates this to better optimization performance (higher best reward, lower regret, more tasks solved).
- **Compelling qualitative examples**: Figure 6 illustrates how the model discovers creative, stable grasps (e.g., rotating an airplane to stabilize it) that the baseline cannot find, demonstrating practical value.

## Weaknesses

### Fatal
None.

### Major
- **No experimental comparison with composite Bayesian Optimization methods**: the paper extensively discusses composite BO (Astudillo & Frazier) as related work and argues its limitations, but does not include a composite BO baseline that could also exploit the auxiliary information within a single task (e.g., a GP on the tactile observations with a learned embedding). Such a comparison would strengthen the claim that the multi-task neural approach is superior and would clarify whether the benefit comes from the across-task representation learning or simply from having a more flexible model.
- **Limited novelty of the architecture**: the core model (Transformer Neural Process with separate context/target encoder) is directly adopted from Nguyen & Grover (2022). The main novelty is the context encoder that processes the auxiliary time series and combines it with (x, f(x)). While this is a reasonable extension, the methodological contribution is incremental relative to the existing literature.

### Minor
- **Modest optimization gain in absolute terms**: the final normalized best value is ~0.85 vs ~0.80 for the baseline after 30 trials. The improvement is statistically significant and consistent, but the gap is not dramatic. The paper's claim of "significantly outperforms" is supported but the practical impact might be modest depending on the application.
- **Model is not updated during optimization**: the authors note this as an advantage (no re-training), but it also means the surrogate cannot adapt to the specific test task beyond the initial context. This could limit performance if the task distribution shifts significantly. A discussion or ablation would be helpful.
- **No ablation on the design of the h(x) encoder**: the context encoder uses a transformer with a [CLS] token and adds an embedding of (x, f(x)). It is not clear how each component contributes. A simpler baseline (e.g., flattening the time series and concatenating with an MLP) could demonstrate the necessity of the more sophisticated encoder.

### Trivial
- The paper states "we treat the addition of auxiliary information by taking the viewpoint of a prior P(F) over the joint function", but the model is trained to predict only f(T) given context that includes h, not to model the joint distribution. This is a minor inconsistency in the framing.

## Nice-to-Haves

- Comparison with a multi-task GP that uses only f to understand the value of the neural architecture beyond classical methods.
- Comparison with a simpler baseline that extracts features from the tactile data (e.g., PCA or autoencoder) and feeds them as additional input dimensions to the f-only surrogate.
- Ablation study of the context encoder design (e.g., removing the (x,f) embedding, using average pooling instead of [CLS]).
- Investigation of how the performance scales with the number of training tasks; the paper uses ~770 training tasks but does not analyze whether performance saturates.

## Novel Insights

None beyond the paper's own contributions: the paper demonstrates that a neural process-style model can effectively exploit high-dimensional auxiliary information across tasks for few-shot design optimization, and provides a concrete benchmark and empirical evidence that this approach outperforms models that ignore such information. The key insight is that learning a representation of the auxiliary information from a history of tasks enables faster identification of high-performing designs on new tasks, especially when only a few evaluations are available.

## Suggestions

- Include a composite BO baseline (e.g., from Astudillo & Frazier 2019 with a GP on learned tactile features) to directly demonstrate the advantage of the multi-task neural approach over single-task methods that also use h(x).
- Add an ablation where the auxiliary information is used in a simpler way (e.g., flattened time series concatenated to x) to justify the sophisticated encoder.
- Consider allowing the model to be fine-tuned on the test task during optimization (or at least discuss the trade-off) to address the fixed-surrogate limitation.

## Score and Decision

**Score**: 6.0

**Decision**: Accept

The paper addresses a novel and practical problem setting with a sound methodology, a strong benchmark, and clear experimental results. The improvements over the baseline are consistent and well-controlled. While the architectural novelty is modest and some comparisons are missing, the overall contribution—especially the benchmark and the demonstration that auxiliary information can be effectively exploited across tasks—provides sufficient value to the community for acceptance.

MY FINAL SCORE: 6.0<score>6.0</score>
MY FINAL DECISION: Accept<decision>Accept</decision>
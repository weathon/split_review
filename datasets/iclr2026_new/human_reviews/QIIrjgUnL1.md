## Human Reviewer 1

### Summary
This paper proposes a position-aware attention mechanism designed to make the standard self-attention more sensitive to relative positions.
It introduces a position-effect and an enhanced position-effect functions which modulates the attention weights according to pairwise positional distance.
The goal is to combine the flexibility of self-attention with an explicit, parametric control over positional bias.
The authors present detailed analyses, including theoretical derivations, simulated experiments on synthetic data distributions (random, structured, clustered, etc.), and consistency metrics comparing theoretical versus actual attention responses.
They claim that this mechanism improves positional interpretability and stability relative to standard Transformers.

### Strengths
1.	Interesting idea: 
The notion of explicitly controlling positional effects via a decaying kernels (Eqs, 1 and 6) is conceptually clean and connects attention to classical signal-processing intuitions about locality.
2.	Analytical exploration:
The paper includes extensive mathematical and empirical analyses of how the proposed positional kernel influences attention behavior.
The “theoretical vs. actual” consistency metric is a thoughtful way to test whether the implementation aligns with the analytical definition.
3.	Comprehensive appendix:
The appendix contains a wealth of supporting materials — visualizations, parameter sensitivity analyses, and ablations — which demonstrate significant effort and curiosity about the model’s internal mechanics.

### Weaknesses
1.	The main text lacks clarity and structure.
Many of the explanations and empirical results appear only in the appendix or not at all.
The main sections barely reference the relevant figures, forcing the reader to guess which figure corresponds to a given discussion.
This significantly reduces readability.
2.	Use of undefined or double-defined formulations.
For example the abstract relates to the parameters $\alpha$, $\beta$ and $\gamma$ without any ability of the abstract reader to understand what they represent…
$P_{effect}$, $A_{ij}$, $V(i)$, $pos^*$ are all defined twice, how do I know which one you mean in the text. Give them a slight differentiator for example $P_{effect}^+$

3.	Limited experimental validation.
The study is conducted almost entirely on synthetic data. There are no evaluations on real tasks (e.g., language modeling or vision benchmarks), so the practical usefulness of the method remains untested.
4.	Ambiguous methodology.
The paper introduces metrics such as $pos_{actual}$ and $pos_{theoretical}$ but does not specify precisely how they are computed,  requiring the reader to reconstruct the procedure themselves. Specifically for these two, there is some reference in the appendix, but I could not find a clear definition. 
5.	Literature positioning is weak.
The paper references related work sparsely. Many strong prior efforts on relative positional encodings (Shaw et al. 2018; Dai et al. 2019; Press et al. 2021; Su et al. 2021) are either missing or only briefly mentioned. On the other hand, all the references in the Abstract makes it cumbersome to follow. It should be precise and short.

### Questions
1. How does this mechanism compare empirically with standard relative position encodings (e.g., RoPE) on real benchmarks?
2. Can the method be integrated into standard Transformer architectures without major computational overhead?
3. Why are key visual results not cited or summarized in the main body? Would the paper benefit from moving Figures A.1–A.8 into the main section?
4. Line 105 – which matrix values do you refer to? I guess it is not $A_{ij}$ because these are all normalized…
5. Line 109 - add “In Fig. 3”…  do so for all references to Figures
6. Line 144 + Figure 6. “Position influence magnitude” was never defined (not also in the appendix AFAIK) 
7. The same goes for other naming in Section 2.3
8. Plenty of typos in citing. lines 035, 037, 039, etc.,
9. Line 207 and Line 863 – what is the difference between $S(pos)$ and $V(i)$
10. I’m not sure what does $I_j$ means. In line 215 I see it is torch.norm(data, dim=-1) is it a the norm over all $i$ values? 
11. Eq. 7. $A_{ij} already include $P_{eff}$. Do we multiply it again by $P_{eff}$?
12. Table 3. I’m not sure I understand. I don’t see any significant difference between architectures. Highest is better or lowest is better?

### Soundness
2

### Presentation
1

### Contribution
3

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper introduces a position-aware attention mechanism designed to address the inherent limitations of conventional attention models, such as those introduced by Ashish Vaswani et al. (2017). The key technical contribution is a positional effect function parameterized by three coefficients: \alpha which controls positional influence intensity, \beta which governs spatial decay rate, and \gamma which compensates for over-attenuation at longer distances. The authors establish the mathematical properties of this function (continuity, differentiability, monotonicity) and propose an adaptive triple-attention architecture integrating position-, task-, and content-aware modules for dynamic weighting. Experiments reportedly demonstrate performance improvements in structured and clustered data scenarios.

### Strengths
1. The paper introduces a positional effect function that offers a formalized mechanism for incorporating positional influence into attention computation.

2. It develops a triple-attention architecture that jointly models position, task, and content information, which is conceptually interesting.

3. It defines quantitative evaluation metrics aimed at measuring attention distribution quality, contributing to more systematic evaluation of attention mechanisms.

### Weaknesses
1. The proposed position-aware attention formulation appears largely as a mathematical restatement of existing positional modulation techniques without a clear, theoretically grounded justification for why it should outperform established methods (e.g., Rotary Position Embedding (RoPE), ALiBi, or relative positional encoding by Peter Shaw et al. (2018)). A stronger theoretical motivation or comparative analysis is needed.

2. The experimental evaluation is insufficiently comprehensive. There are no direct comparisons with strong baselines such as RoPE, ALiBi, or Shaw et al. on realistic benchmarks (e.g., long-document modeling, QA).

3. The implementation details are incomplete or unclear. Important information about model architecture, parameter sizes, training setups, and hyperparameters are missing, which prevents reproducibility.

4. Some core concepts lack precise definition or justification. For example: I_j in Eq. (3) and (4) is referred to as “information importance,” but its definition and computation are not explained. The proposed “consistency” and “ranking correlation” metrics are not well motivated or compared against established alternatives.

5. The claim that the triple-attention architecture achieves superior performance is not strongly supported by the results in Table 3, where the improvements over other configurations are marginal.

6. The description of experimental results is ambiguous: it is unclear whether larger or smaller metric values indicate better performance, and some tables lack sufficient explanation.

### Questions
1. Please include experimental comparisons with strong and widely recognized baselines (e.g., RoPE, ALiBi, Shaw et al. 2018) to substantiate the claimed advantages of the proposed method.

2. Please provide a clearer and more rigorous definition of I_j and its role in the method. Also, please justify the choice of evaluation metrics or align them with established practices in the field.

3. Please clarify how to interpret each evaluation metric (e.g., whether higher or lower is better) and provide more structured and detailed explanations of results.

4. Please include comprehensive implementation details, such as model configurations, training setup, hyperparameters—to facilitate reproducibility and fair comparison.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper introduces a position-aware attention mechanism that explicitly models positional relationships in attention computation through a position effect function, parameterized by $\alpha$ (intensity) and $\beta$ (decay). It mathematically analyzes their properties (continuity, differentiability, monotonicity) and proposes an enhanced variant with an additional $\gamma$ coefficient to mitigate over-attenuation in long-distance dependencies. Built on this, the authors develop a triple-attention architecture incorporating position-aware, task-aware, and content-aware attention to achieve task-specific flexibility.

### Strengths
The quality of the Appendix seems better than the main text

### Weaknesses
1. It is not clear why the proposed position effect function addresses the limitations of traditional attention mechanisms by providing fine-grained control over positional relationships, as stated on line 94-96. Or what’s the advantage to existing methods like relative positional encoding and ROPE? If it’s only about modeling the dependency between $i, j$, ROPE also mathematically supports this, no?
2. I am confused of section 2.2. What is the analysis subject to? On lines 105-106, the author states, “Specifically, α = 0.5 yields maximum values of approximately 0.5, α = 1.0 produces values of 1.0, α = 2.0 generates values of 2.0”. But there is no explanation of what the values impacted by the $\alpha$ values refer to.
3. Experiment section is not clear enough in introducing the settings such as data, model, baselines.
4. Eq.1 seems redundant as it is introduced again from line 92
5. Typo, Line 357: we previously -> our previously

### Questions
Is it better to rearrange so that the analysis in section 2 appears later, say the experiment section?

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes a position-aware attention mechanism that extends traditional Transformer attention (Vaswani et al., 2017) by incorporating a novel positional effect function. The method builds upon relative position representations (Shaw et al., 2018) and rotary position embeddings (Su et al., 2021), introducing parameters α and β to control positional influence and spatial decay rate. To alleviate long-distance over-attenuation, the authors further introduce an enhancement coefficient γ and design an adaptive triple-attention architecture that integrates task-aware and content-aware modules for dynamic weight adjustment. The paper also provides theoretical analysis on the proposed function’s properties (continuity, differentiability, monotonicity) and introduces new evaluation metrics for consistency and positional benefit. Experiments demonstrate promising results on structured and clustered datasets, particularly for information retrieval and document understanding tasks.

### Strengths
Theoretical novelty: The paper provides a mathematically grounded extension to existing position encoding methods, offering interpretable control of positional influence and decay behavior.

Innovative architecture design: The proposed adaptive triple-attention framework with task- and content-aware weighting is conceptually interesting and well-motivated by recent multi-scale attention work.

Clear motivation and formulation: The paper is well-written and logically structured, clearly explaining the motivation behind each modification to the standard attention mechanism.

Potential practical impact: The approach could improve transformer interpretability and adaptability in tasks where fine-grained positional relationships are important.

### Weaknesses
Limited empirical validation: While the theoretical contributions are strong, the experimental section is relatively weak. The evaluation mainly covers structured and clustered datasets, without sufficient diversity to support claims of general effectiveness.

Computational analysis: No discussion on computational cost, convergence, or scalability compared to baseline attention mechanisms

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
3
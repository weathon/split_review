## Summary

This paper presents the first systematic complexity-theoretic analysis of circuit discovery queries for inner interpretability on multi-layer perceptrons. It formalizes a comprehensive set of circuit queries (sufficient circuits, gnostic neurons, circuit ablation/clamping, patching, necessary circuits, robustness) and settles the classical complexity, parameterized (in)tractability, and approximability of many variants. Key contributions include proving that most variants are intractable (NP-hard, Σ^p_2-hard, W[1]-hard) and inapproximable; introducing quasi-minimality as a tractable relaxation that retains useful affordances; establishing a formal separation between local and global query complexity that explains observed "interpretability illusions"; and tightening existing results on Sufficient Reasons.

## Strengths

- **First systematic complexity treatment of circuit discovery for inner interpretability.** The paper fills a gap explicitly noted as an open problem (lines 81–88). Table 1 maps ~20 problem variants across 7 query types to complexity classes, parameterized hardness, and approximation inapproximability — a scope unmatched by prior work on explainability (Barceló et al., 2020; Bassan & Amir, 2024), which focused on input queries rather than circuit queries.

- **Quasi-minimality as a tractable relaxation with genuine utility.** The paper introduces quasi-minimal sufficient circuits (UQLSC, PTIME) and quasi-minimal patched circuits (UQLCP, PTIME) — moving from NP-complete minimality to polynomial-time tractability while retaining the "breaking point" property that enables ablation-based interventions (lines 282–294, 347–355, Table 1). This is a novel construction with direct practical relevance.

- **Formal separation between local and global query complexity.** Local Sufficient Circuit is NP-complete while global Sufficient Circuit is Σ^p_2-complete (lines 271–274). This formal separation directly explains "interpretability illusions" (Friedman et al., 2024) — local faithfulness is verifiable at NP-level complexity, but global faithfulness requires strictly higher complexity, so methods that achieve local faithfulness can systematically fail at global faithfulness. The pattern holds across CA, CC, CP, NC, and CR variants (Table 1).

- **Inapproximability results across five approximation schemes.** Hard variants of SC, CA, CC, CP, and NC are inapproximable under additive (c-approximation), multiplicative (PTAS), and all three probabilistic (3PA) schemes (lines 269, 328, 343, 424; Table 1). This rules out common escape hatches from intractability — not just exact solutions but also approximate, randomized, and average-case polynomial-time approaches.

- **Tightened existing results on Sufficient Reasons.** Using proof techniques developed for circuit queries, the paper improves prior results (Barceló et al., 2020) by proving hardness holds even when the MLP has only a single hidden layer (line 459), demonstrating the framework's transferability beyond inner interpretability.

- **Fixed-parameter tractability for Circuit Robustness under a natural parameter.** Circuit Robustness parameterized by |H| (size of the hypothesized robust set) admits FPT algorithms for both local and global variants (lines 401–402, Table 1) — a nuanced positive result that provides concrete algorithmic recommendations for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **The activation function of the MLP is not specified in the main text.** This is the paper's most consequential presentation gap. The complexity of any query on an MLP depends on what function each neuron computes (threshold/step, ReLU, linear, etc.). The paper defers formal model definitions to the appendix (lines 101, 190, 230, 241, 250), which is parser-stripped, but the main text itself should state the neuron computation model — every theorem's validity is conditional on this assumption. The results are almost certainly correct under standard assumptions (e.g., ReLU or threshold gates with rational weights, which are the implicit standard in the neural network complexity literature), but not specifying this forces the reader to guess at critical modeling choices. This is structural to the presentation, not fatal — it can be straightforwardly resolved by stating the assumption — but it is the paper's clearest weakness and an unusual omission for a formal complexity paper.

### Minor

- **Parameterization granularity for W[1]-hardness of SC.** For Sufficient Circuit, the table reports "$\mathcal{P}$-SC" as W[1]-hard where $\mathcal{P} = \mathcal{P}_\mathcal{M} \cup \mathcal{P}_\mathcal{C}$ (the full parameter set including depth, width, weights, biases, etc.). The text claims "hardness is not mitigated by keeping models shallow" (line 268), implying depth alone was analyzed, but the table does not break out which specific parameters drive hardness for SC. For other queries (CA, CC, CR, NC) the table lists specific parameter subsets that cause hardness, making the SC row less informative. The paper would be stronger with per-query parameter-specific results.

- **The connection between ACDC and quasi-minimality is suggestive, not proven.** The discussion (lines 468–473) claims Conmy et al.'s ACDC algorithm "is well-equipped to solve Quasi-Minimal Circuit problems" and offers a binary-search speedup hint, but provides no formal argument that ACDC's edge attribution patching procedure actually solves UQLSC or UQLCP as defined. This is presented as post-hoc reasoning rather than a proven correspondence. While this does not detract from the paper's formal results, it overstates the explanatory connection to existing heuristics.

### Trivial

None.

## Nice-to-Haves

- Including a sketch of one concrete reduction (e.g., from SAT to Local Sufficient Circuit) in the main text would improve pedagogical value and force explicit modeling assumptions to be stated upfront.
- For SC and other queries where W[1]-hardness is reported with the full parameter set, providing finer-grained parameterization results (as is done for CA, CC, CR, NC) would strengthen the parameterized complexity contribution.
- Clarifying in the main text how $\mathcal{C}(\mathbf{x})$ is precisely evaluated when $\mathcal{C}$ is a strict subset of neurons that may not form an end-to-end connected subgraph (currently deferred to the appendix).

## Removed Points

The following points from the input reviews were removed per filtering rules:

- **Quasi-minimality PTIME claims lacking specified computational model (Harsh Critic #2):** The paper repeatedly defers algorithm details and formal definitions to the appendix (\ref{app}), which is parser-stripped. Hard rules require removing weaknesses predicated on missing appendix content.
- **Gnostic Neuron input representation concern:** Speculation that complexity could change if input sets were implicitly described. The problem definition provides them as explicit sets, making the PTIME claim clearly valid. Speculative concern removed.
- **Inapproximability claim strength:** Comment about inapproximability relying on complexity assumptions is standard practice in the field, not a paper-specific weakness.
- **"Circuit inference" missing definitions:** Formal definitions are stated as deferred to the appendix; hard rules apply.
- **Pure formatting/style nitpicks and requests for complete training logs:** Removed under hard rules.
- Several generic "one-size-fits-all" concerns from the harsh critic's section-by-section sweep that lacked concrete anchors in the paper text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Specify the activation function (or class of activation functions) and arithmetic model (rational vs. real numbers) explicitly in the model architecture section of the main text.
- For SC, break out which specific parameter subsets cause W[1]-hardness, as is done for other queries, rather than reporting only the full parameter set.
- Tone down or formally ground the claim that ACDC "solves" quasi-minimal circuit problems; the current discussion language overreaches what the paper demonstrates.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
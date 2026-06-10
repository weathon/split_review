## Summary

The paper proposes DIRAD, a structural adaptation method that grows networks from minimal initial topologies via an Edge-Node Conversion (ENC) mechanism designed to escape "statistical conflicts" (per-sample gradient cancellation). It then extends this into PREVAL, a continual learning framework that uses an auxiliary L1 prediction network to detect new tasks from prediction mismatches and route samples to appropriate models without requiring task labels. Experiments on a 3-task downscaled MNIST benchmark show retention of 85–94% when new tasks are detected, with network complexity orders of magnitude below fully-connected alternatives.

## Strengths

- **DIRAD produces extremely compact networks with documented complexity ratios.** The paper reports that 2-class MNIST problems are solved with 6–20 hidden nodes and 15–50 edges, compared to 3,296 edges for a single-hidden-layer fully-connected network of 16 neurons (Section 5, line 157). This is a concrete, quantified advantage that the paper backs with specific run data.

- **PREVAL demonstrates continual learning without task labels, with diagnostic breakdown of failure modes.** Table 2 shows retention ratios of 0.85–1.01 (ALL+3) across four $T_{CP}$ settings, with 0.87–0.94 when runs with undetected tasks are excluded. The experimental design separates detection failures from discernment failures (Table 1), a diagnostic approach more informative than pooled numbers alone, and directly identifies detection as the primary bottleneck (line 168).

- **The L1 network design constraint against trivial solutions is well-motivated.** Section 4 (line 112) explicitly prevents L1 from replicating L0 pathways: "no node $n_1 \in L0$ can have a path to $n_0$ via L1 if it also has a path to $n_0$ via L0." The reasoning about why autoencoders and overparameterized alternatives would fail in this role (lines 143–144) is articulate and frames DIRAD's suitability for the PREVAL architecture.

- **The paper is transparent about its own limitations.** It explicitly flags DIRAD's computational cost and incompatibility with hardware acceleration (line 213), acknowledges theoretical upper bounds on task discernability that tuning cannot overcome (line 217), states that the current implementation foregoes transfer learning (line 223), and clarifies that the mechanisms are not biologically plausible (line 12).

## Weaknesses

### Fatal

None.

### Major

- **No comparisons against standard continual learning baselines.** The paper evaluates PREVAL against theoretical lower bounds (random classification, latest-task-only perfect response) but never against any established CL method — not EWC, GEM, SI, Progressive Networks, or any architecture-based alternative. This is especially problematic because the paper stakes a priority claim ("first framework that can handle continual adaptation with high accuracy & retention of past information while doing both new task detection & discernment… without task labels," line 217). Without baselines, it is impossible for a reader to assess whether PREVAL advances the state of the art or merely demonstrates a working proof-of-concept.

- **The central theoretical claim about ENC resolving statistical conflicts is not substantiated.** The ENC mechanism is the paper's core technical innovation — the thing that distinguishes DIRAD from prior structural adaptation methods. Yet the paper states explicitly that the condition in Equation (95) "was not verified mathematically" and that the conjecture that it "may correspond to a global optimum" is only an intuition (line 98). The paper provides an illustrative signed-XOR example (Figure 1) but no controlled experiment demonstrating that ENC specifically (rather than simple edge addition or the priority ordering scheme) is responsible for escaping gradient cancellation. A method whose central mechanism operates without theoretical or ablation-based validation cannot support the claims made for it.

- **No ablation studies.** DIRAD has multiple interacting mechanisms (edge generation, ENC, priority ordering, the specific modulatory node design with its multiplicative structure and bespoke transfer function $\sigma_1(x) = 4/(1+e^{-Kx})-1$ where $K=1/w_{ij}$). PREVAL has four thresholds ($T_{CP}$, $T_{conf}$, $T_{SV}$, $\epsilon_{IS}$). The experiments vary only $T_{CP}$ across four values. There are no ablations isolating ENC vs. simple edge addition, no comparison against a version without modulation, no sensitivity analysis for $T_{conf}$ or $T_{SV}$, and no study of whether simpler priority ordering schemes would suffice. The paper cannot attribute its results to any specific component.

- **Overclaiming given the evidence.** The paper claims PREVAL is "the first framework that can handle continual adaptation with high accuracy" (line 217). The reported results show 67–71% net accuracy after 3 tasks on a single downscaled MNIST benchmark, with new task detection failing in up to 3/8 runs. "High accuracy" is not supported by these numbers, and "first" is a strong claim unsupported by the literature review or experimental comparison.

### Minor

- **Evaluation is limited to a single benchmark with minimal scale.** Downscaled MNIST (14×14) with only 3 binary tasks (2 classes each) and no other dataset (no CIFAR variant, no permuted-MNIST, no miniImageNet) is far below standard CL evaluation protocols. Split-MNIST typically uses 5–10 tasks, and modern CL papers routinely evaluate on multiple benchmarks.

- **Weak statistics.** Only 8 runs per condition are reported, with no confidence intervals or standard deviations. For $T_{CP}=0.15$ and $0.20$, three of eight runs had undetected tasks, meaning the conditional averages (inside parentheses in Table 1) are based on only 5 runs.

- **Critical hyperparameters not specified.** The values of $T_{conf}$, $T_{SV}$, and $\epsilon_{IS}$ used in the experiments are never stated. Only $T_{CP}$ is reported (0.05, 0.10, 0.15, 0.20). This is a reproducibility concern.

- **No analysis of network growth dynamics across the continual learning scenario.** The paper reports L0 complexity for a single task (6–20 nodes, 15–50 edges) but not how complexity evolves across the full 3-task PREVAL scenario. Does growth explode or stabilize? Are models reused or always created from scratch?

- **No computational cost measurements.** The paper acknowledges DIRAD's computational complexity (line 213) but provides no wall-clock time, FLOP counts, or comparison to NN training cost. With strengths being predicated on "orders of magnitude simpler" networks, some cost measurement is needed.

- **Retention ratios exceeding 1.0 are not clearly explained.** At $T_{CP}=0.10$, ALL+3 (net accuracy ratio after 3 tasks) is 1.01, meaning accuracy *increased* after adding more tasks. The paper notes this in passing but does not explain whether this reflects easier later tasks, a quirk of the metric, or some other phenomenon.

- **Technical concerns about the ENC design are unaddressed.** The multiplicative structure in Equation (44) creates complex gradient pathways whose stability is not analyzed. The transfer function $\sigma_1$ has steepness $K=1/w_{ij}$ inversely tied to the original edge weight — a design that could be fragile if $w_{ij}$ is very small or large, with no sensitivity analysis provided.

### Trivial

None.

## Nice-to-Haves

- Ablation studies isolating the contribution of ENC vs. simple edge addition.
- Evaluation on standard CL benchmarks (split-MNIST at 5/10 tasks, permuted-MNIST, split-CIFAR-100).
- Confidence intervals or standard deviations for all reported metrics.
- Full disclosure of hyperparameter values used ($T_{conf}$, $T_{SV}$, $\epsilon_{IS}$, learning rate, batch size, stabilization criterion).
- Wall-clock time or FLOP measurements.
- Analysis of network growth (nodes and edges) across the full CL scenario.
- Code release to aid reproducibility of this complex method.

## Removed Points

These points were identified by reviewers but removed after verification against the paper:

- **"No specification of how L1 nodes are selected as target nodes"** — The paper explicitly states (line 112): "Target nodes of L1 are all the nodes (including inputs) in L0 except output nodes." This is a factual error by the reviewer.

- **"Background on continual learning is thin / engages with too few works"** — The paper cites relevant works (Rusu et al. 2016, Kirkpatrick et al. 2017, Jacobson et al. 2022, Hadsell et al. 2020, Parisi et al. 2019) and frames its contribution relative to them. The criticism is a category-driven area-of-concern sweep without a specific gap identified.

- **"No code or reproducibility materials are mentioned"** — This is standard for a conference submission; code availability is typically handled post-acceptance. Not a weakness of the paper's intellectual content.

- **"ENC provides a principled architectural escape from conflicting gradients" (as a claimed strength)** — This conflicts with the verified weakness that the ENC mechanism is not theoretically validated and lacks ablation evidence. Per the filtering rules, when a strength and weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known tensions (unvalidated core mechanism, thin empirical support, overclaiming) that are standard structural critiques of early-stage method papers, without adding a novel synthesis.

## Suggestions

- **Add standard CL baselines** — At minimum, compare PREVAL against EWC, Progressive Networks, and a no-protection baseline on the same 3-task setup. Even if direct comparison is imperfect due to different assumptions (task-label-free vs. task-labeled), showing relative performance gives readers essential context.

- **Validate the ENC mechanism in isolation** — Run a controlled comparison where DIRAD with ENC is compared against (a) DIRAD without ENC (edge addition only) and (b) a fixed-topology network, on a simple task where gradient cancellation demonstrable occurs. Report gradient norms before and after ENC to show the mechanism works as claimed.

- **Scale up the evaluation** — Add at least one more benchmark (e.g., permuted-MNIST or split-Fashion-MNIST) and increase to 5+ tasks. Report per-task accuracies in addition to net accuracies so forgetting can be measured directly.

- **Tone down priority claims** — Remove or soften "first framework" (line 217) and "orders of magnitude" generalization beyond what is directly measured. The current evidence supports a proof-of-concept, not a claimed first-in-class result.

- **Report all threshold values** — Disclose the exact values of $T_{conf}$, $T_{SV}$, and $\epsilon_{IS}$ used. Report standard deviations or confidence intervals for all accuracy metrics.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
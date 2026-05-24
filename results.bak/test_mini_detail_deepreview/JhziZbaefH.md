Now I have everything I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes OML, a brain-inspired hierarchical modular neural network for online multimodal learning. The network uses feature neurons, unimodal/multimodal association neurons, ascending/descending/lateral pathways, a reference extraction algorithm (coefficient of variation to identify which feature dimensions a word refers to), and conflict detection with human-in-the-loop interaction. Experiments on small visual-auditory (Fruits, HomeF) and visual-auditory-taste (VAT) datasets show OML outperforms existing online methods (ART, AEN) across close and open environments, and particularly demonstrates the ability to learn precise word references (e.g., color vs. object name).

## Strengths

1. **Reference extraction via coefficient of variation is a genuine algorithmic contribution.** Section 3.4 defines a principled mechanism that autonomously identifies which feature dimensions a word refers to by tracking variance stability across samples. Table 2 shows this delivers a clear edge: OML achieves 87.3% (V→A, E-Fruits close) while offline methods drop 10+ points (marked ↓) because they cannot distinguish name words from attribute words. Prior online methods (ART, AEN) lack this capability entirely.

2. **Conflict detection is demonstrated experimentally.** Section 4.1(3) reports that when 10% of word-image or word-taste pairs were intentionally mismatched, OML detected *all* conflicts and raised appropriate questions. This ability to identify inconsistent input-pairs during online learning is absent from prior online multimodal methods (Xing et al., Shubham et al.).

3. **Modality extension with precise cross-modal routing.** Table 3 shows OML outperforms AEN on all cross-modal recall tasks when a taste channel is added (e.g., T→V 90.1 vs. 88.3, VAT close). The frequency-parameter-based routing (Eq. 6) enables OML to activate the correct modality-specific concept, so "tián" (taste) and "hóng sè" (visual) each recall from the right channel — something AEN cannot distinguish.

4. **Competitive open-environment performance.** In the open environment (Table 1), OML maintains stable accuracy (e.g., Fruits V→A: 89.2 close → 89.8 open) while offline methods drop substantially (DBM: 70.5 → 54.3). OML also outperforms other online methods (ART, AEN) in this setting, demonstrating effective lifelong learning without catastrophic forgetting.

## Weaknesses

### Fatal
None.

### Major

1. **The human-in-the-loop interaction is not actually tested — only conflict detection is validated.** The paper's headline claim (2) states the network can "ask the user appropriate questions and conduct learning based on user's answer." However, Section 4 states: *"if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive"* (line 244). The method in Section 3.5 specifies both positive-answer and negative-answer pathways (lines 179–180), but in the experiments every conflict effectively resolves to "yes" — the effect of negative answers is never evaluated. The conflict *detection* itself is tested (10% mismatched pairs), but the interactive learning loop with non-positive answers is not. Without testing scenarios where the simulated user says "no," the claimed human-in-the-loop capability remains unvalidated. *Evidence: Lines 179–180 describe both answer types; line 244 shows only positive answers are used in practice.*

2. **No ablation studies, so contributions of individual components are unknown.** The model has many interacting mechanisms: frequency-based neuron activation (Eq. 1), the reference extraction threshold (Eq. 7, parameter r), lateral connections (Section 3.1, L matrices), conflict detection (Section 3.5), the dynamic neuron/connection addition, and the descending signal Gaussian model (Eq. 2). Without any ablation, the accuracy improvements in Tables 1–3 cannot be attributed to any specific design choice. For instance, the reference extraction is claimed as crucial for the Table 2 results, but there is no experiment comparing OML with and without it. The improvements could plausibly stem from the network's structural growth capacity alone. *Evidence: Section 4 contains no ablation experiments.*

3. **Open-environment comparison with offline methods is misleadingly framed.** The paper states: *"In the open environment, the accuracy of the offline methods drops significantly due to the catastrophic forgetting"* (line 250). However, offline methods are frozen after training; in the open-environment protocol where *"we divide the dataset into four equal parts, each containing different classes"* (line 227), these methods are trained only on the first part and never see the remaining classes. Their accuracy drop on later parts is not "catastrophic forgetting" — it is failure to generalize to unseen classes. The online vs. online comparison (OML vs. ART vs. AEN) is valid and informative, but attributing the offline methods' drop to forgetting is incorrect and undermines the paper's claim about anti-forgetting. *Evidence: Lines 227, 250.*

4. **Results lack error bars or statistical significance.** All accuracy numbers in Tables 1–3 are presented as single values without variance estimates, confidence intervals, or significance tests. Given that differences between methods are sometimes modest (e.g., OML 89.2 vs. AEN 85.1 in Table 1 close — a 4.1% gap), it is impossible to assess whether these differences are meaningful. *Evidence: Tables 1–3 show only single numbers.*

### Minor

1. **Datasets are small and use hand-crafted features.** The experiments use Fruits (~common fruits) and HomeF (~home objects), with features extracted via Fourier descriptors (shape) and MFCCs (audio) — not deep features. While these datasets follow prior work (Xing et al.), they limit claims about scalability to real-world multimodal data with natural language. Extending to a standard multimodal benchmark would strengthen the paper.

2. **Hyperparameter sensitivity is not analyzed.** Parameters (θ = quarter of weight norm, T = 150, ϑ = 0.8, r = 0.5) are given without any sensitivity study. The threshold θ in particular determines when new feature neurons are created, which is central to the model's growth behavior. *Evidence: Parameter values listed in lines 227–228.*

3. **Catastrophic forgetting is not directly measured.** The paper claims OML avoids catastrophic forgetting but never reports forgetting explicitly (e.g., accuracy on previously learned classes after learning new ones). The open-environment results show final accuracy on a held-out test set, which aggregates performance across all classes. A direct measure of backward transfer would strengthen the claim. *Evidence: Section 4 does not report per-task or per-class forgetting metrics.*

4. **The method description is dense and would benefit from pseudocode.** The architecture involves many interacting equations (Eqs. 1–8) and procedural rules (four learning scenarios in Section 3.5). A step-by-step algorithm listing would significantly improve reproducibility and clarity.

### Trivial
- Several figure descriptions are duplicated in the text (e.g., lines 19–31 contain the same caption repeated three times for Figure 1). These are parser artifacts and should be deduplicated in the actual submission.
- Equation (1) includes a cosine term over T=150 time steps, described as *"its value does not affect the algorithm"* (line 75). If the term does not affect the algorithm, its role should be clarified or simplified to avoid confusion.

## Nice-to-Haves
- **Test the interaction with negative answers:** A controlled experiment where some conflicts receive simulated "no" answers would directly validate the human-in-the-loop claim.
- **Ablate the reference extraction mechanism:** Compare OML with a version that treats all feature dimensions equally when learning word associations. This would isolate the contribution of Section 3.4.
- **Run a proper open-environment protocol for offline methods:** Either retrain them incrementally on each part or clearly state they are baselines for "no adaptation" and remove the "catastrophic forgetting" framing.
- **Report results over multiple random seeds** with variance and, where appropriate, pairwise significance tests.
- **Add a direct forgetting measure** (e.g., accuracy on task 1 after learning task N) to Table 1's open environment.

## Removed Points

These points were flagged by reviewers but are removed or downgraded in the final review; treat them with caution.

1. **"The comparison with offline methods in the open environment is almost certainly unfair and likely invalid"** — Retained but downgraded from Fatal to Major. The comparison between online methods is valid and informative; the issue is specifically the *framing* of why offline methods fail, not the comparison itself. This is a standard (if imprecise) continual-learning evaluation practice.

2. **"The method description is confusing and under-specified"** (various sub-points about Eq. 1's cosine term, the Gaussian model, etc.) — These are retargeted into Minor points above. The description is detailed but dense; the core mechanisms are present and derivable. The request for pseudocode is moved to Minor/Nice-to-Have.

3. **Strength Finder claim about "hierarchical modular architecture with explicit pathways" being a core strength** — Removed. This describes the method architecture itself, which is necessary for the method to exist but not a demonstrated strength beyond what the experimental results already support. The experimental results (Tables 1–3) already serve as the evidence; listing the architecture as a separate strength without additional evidence is circular.

4. **Strength Finder claim about "human-in-the-loop interaction" being a fully validated strength** — Demoted. Conflict detection is validated (10% mismatched pairs, all detected), but as noted in Major weakness 1, the interactive loop with negative answers is not tested. The strength is partial.

5. **Harsh Critic's claim that the offline methods' poor performance in Table 2 is "not because they cannot learn precise referring"** — Removed. The paper's Table 2 comparison is valid: offline methods trained on the full dataset in the close environment drop in accuracy when color words are added because their static representations cannot distinguish attributes from object names. The drop-marking (↓) is appropriate, and the paper's interpretation is reasonable.

## Novel Insights

The reviews surface an important tension: the paper's architecture genuinely addresses an underexplored problem (learning precise word references and detecting conflicts during online multimodal learning), but its experimental methodology does not match the ambition of its claims. The most interesting finding from synthesis is that the reference extraction mechanism (coefficient of variation over descending signals) is novel and demonstrated with reasonable evidence in Table 2, while the human-in-the-loop aspect — arguably the paper's most distinctive claim relative to prior online multimodal work — is the weakest-supported part. This asymmetry suggests the paper's core durable contribution is the reference extraction and hierarchical growth architecture, not the interaction mechanism, which the authors could productively reframe.

## Suggestions

1. Conduct an experiment with simulated negative answers to validate the human-in-the-loop mechanism directly.
2. Add at minimum one ablation: remove reference extraction and report whether Table 2 results collapse.
3. Report all main results over ≥5 random seeds with standard deviations.
4. Redesign the open-environment framing: either retrain offline methods incrementally (with replay or fine-tuning) or clearly state they serve as "no-adaptation" baselines, removing the "catastrophic forgetting" label for their accuracy drops.
5. Provide pseudocode for the online learning algorithm (Section 3.5's four scenarios) to aid reproducibility.

## Score and Decision

**Calibration protocol:**

**Round 1 (Bracketing):** Three queries on topics related to online multimodal learning, lifelong learning, and brain-inspired architectures. Weak-band anchors (avg 2.0–3.33) were rejects with major methodological flaws. Middle-band anchors (avg 4.0–6.5) included both rejects and accepts. Strong-band anchors (avg 8.0–9.0) were accepts with thorough experimentation and clear contributions. Initial bracket: **[3.5, 5.5]**.

**Round 2 (Narrowing):** Two targeted queries inside (3.0, 5.5) for brain-inspired and small-dataset continual learning papers. Anchors read in full:

- **JAnyCnK5In** (avg 4.75, reject) — Online SNN training paper. Mixed reviews (5,3,6,5). Criticized for lacking novelty despite integrating multiple existing ideas. Our paper has *more* novelty (reference extraction, conflict detection) but *weaker* experiments (no ablations vs. their standard benchmarks on CIFAR/ImageNet). Our paper is slightly weaker overall → my score should be somewhat below 4.75.

- **jYyste2HLP** (avg 4.33, reject) — Bio-inspired incremental orientation learning. Tested on a single challenging dataset. Our paper has more extensive evaluation (multiple datasets, multiple tasks) but shares similar weaknesses (no error bars, niche datasets). Comparable quality; our paper is slightly stronger → my score should be at or above 4.33.

- **9aZ2ixiYGd** (avg 5.0, accept; scores 8,6,3,3) — Prompt-based continual learning with thorough ablations, multiple large-scale datasets (CIFAR100, ImageNet-R, CUB), theoretical analysis. Clearly stronger than our paper in experimental rigor. My score should be well below 5.0.

- **CagdoUkvvl** (avg 4.5, reject) — Multimodal continual learning with dual-learner + relaxed contrastive. Included ablation studies. Our paper has more novel architecture but weaker experiments. Slightly below this anchor.

**Final position:** Between the 4.33 (FlyOrien) and 4.75 (SNN online) anchors, closer to the lower end given the open-environment framing issue, lack of ablations, and untested interaction. Against the 5.0 accept, our paper clearly lacks the experimental completeness required for acceptance.

**Score: 4.0 — Reject.** The paper proposes genuinely novel ideas (reference extraction, conflict detection for online multimodal learning) and presents evidence for some claims. However, the experimental validation has three significant gaps that collectively prevent acceptance: (a) the human-in-the-loop interaction is claimed but not tested with negative answers, (b) no ablation studies isolate which components drive performance, and (c) the open-environment offline comparison is misleadingly framed. These issues can be addressed with additional experiments, and a revised submission would be worth reconsidering.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
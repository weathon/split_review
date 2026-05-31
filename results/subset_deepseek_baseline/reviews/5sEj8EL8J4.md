## Summary

The paper proposes a cross-modal attention framework for multi-agent reinforcement learning (MARL) in collaborative coding, where agents coordinate through both structured code (abstract syntax trees) and natural language messages. The framework uses a graph neural network to encode ASTs, a pretrained Transformer for language messages, and weakly supervised contrastive learning driven by code execution outcomes to align the two modalities. Syntax-aware attention gates restrict message influence to syntactically relevant code regions. Experiments on two collaborative coding benchmarks report improvements over three baselines.

## Strengths

- The problem of aligning structured code representations with unstructured natural language in a multi-agent setting is practically relevant and underexplored.
- The use of execution feedback (pass/fail, runtime errors) as a weak supervision signal avoids expensive manual annotation, which is a practical advantage.
- The syntax-gated attention mechanism is a reasonable design choice to prevent semantically irrelevant messages from affecting code reasoning.

## Weaknesses

### Fatal
None that invalidate the core claims, but several major issues severely weaken the contribution.

### Major

1. **Insufficient novelty relative to existing work.** The framework is a straightforward combination of established components: GNN, pretrained language model, contrastive learning, and multi-agent PPO. The claimed contributions—cross-modal alignment with weak supervision and syntax-aware attention—are not adequately differentiated from prior work. For instance, Solaiman & Bhargava (2022) already use execution-based weak supervision for cross-modal alignment, and the syntax gating is a simple depth/type mask rather than a learned mechanism.

2. **Lack of clarity and missing technical details.** Critical aspects of the method are ambiguous:
   - The alignment loss (Eq. 4) uses a binary label \(y\), but how \(y\) is derived from execution outcomes is never explained. Is it a single pass/fail? Which code-message pairs correspond to a positive vs. negative label?
   - The contrastive learning formulation (Eq. 10–12) is vague: how exactly are positive and negative pairs defined? The paper says “negative samples are drawn from within the same batch, using execution outcomes as weak supervision,” but the construction of pairs is unclear.
   - The dynamic embedding refinement (Section 4.3) adds an alignment reward \(r_a\) (Eq. 13) directly into the critic. This risks reward hacking (maximizing alignment without improving task performance) and the interaction between the two objectives is not analyzed.
   - The syntax mask \(M_{ik}\) (Eq. 7) requires heuristically chosen thresholds \(\tau\) and type sets \(\mathcal{T}_k\). No sensitivity analysis is provided.

3. **Weak experimental evaluation.**
   - Only three baselines are compared, none of which are modern multi-agent communication protocols (e.g., CommNet, IC3Net, TarMAC, or other attention-based MARL methods). The best baseline (“Syntax-NL Heuristics”) uses handcrafted rules, making it a weak comparator.
   - The datasets (CodeReviewNet, CollabCode) are not standard benchmarks for multi-agent coding. No details are given about the number of agents, observation spaces, action spaces, or inter-agent communication structure.
   - The ablation study (Table 2) shows component contributions but is incomplete: it does not ablate the contrastive learning objective, the execution-based weighting of negatives, or the specific design of the attention gate (e.g., replacing it with a learned strategy).
   - Attention patterns are shown qualitatively (Figure 3/4), but no quantitative metrics (e.g., precision/recall of relevant node identification) are reported.
   - The claim of “24.8% higher TSR” is computed relative to the best baseline (63.4% → 78.9%), but absolute improvement is 15.5 percentage points, which is less impressive.

4. **Potential overclaiming.** The paper states “We make collaborative coding a formal cross-modal MARL problem” as a contribution. However, prior work (Yu et al., 2024; Hong et al., 2024) already considers code and language in MARL settings, albeit with different approaches. The formulation does not appear to introduce new formalism.

### Minor

- The paper refers to figures (Figure 2, 3, 4) that in the provided text are replaced by tables (likely a parsing artifact), making the results hard to interpret.
- Some references seem tangential (e.g., Bille (2005) on tree edit distance is cited for ASTs but not used; Okken (2022) is a pytest book rather than a research method).
- The ethical considerations section is generic and not specifically tied to the proposed framework.

### Trivial

- The abstract contains “The harmful effect of such work is three-fold” – likely a typo for “contribution”.
- Several sentences are poorly structured, but per guidelines we do not penalize formatting issues.

## Nice-to-Haves

- Compare against modern multi-agent communication baselines (TarMAC, IC3Net, VBC) and other cross-modal code-language models (e.g., CodeBERT-based alignment without MARL).
- Provide a pseudocode or detailed algorithm for the training loop and contrastive pair construction.
- Include quantitative evaluation of attention quality (e.g., do syntax gates actually improve grounding accuracy?).
- Analyze sensitivity to hyperparameters \(\tau\) (depth threshold), \(\mathcal{T}_k\) (type sets), \(\beta\) (alignment weight), and \(\lambda\) (negative weighting).

## Novel Insights

None beyond the paper’s own contributions. The work presents a plausible recipe for combining existing techniques, but does not yield a fundamentally new understanding of cross-modal learning or multi-agent coordination.

## Suggestions

- Clearly define how execution outcomes produce binary alignment labels and how positive/negative pairs are formed in contrastive learning.
- Add comparisons with state-of-the-art MARL communication methods and with cross-modal learning baselines adapted from vision-language tasks.
- Provide ablation studies on the weak supervision parameters (e.g., different definitions of y, weighting strategy) and on the attention mask design (e.g., learned vs. heuristic gating).
- Show convergence properties and variance across multiple random seeds.

## Score and Decision

The paper addresses a relevant problem but suffers from limited novelty, insufficient technical clarity, and weak experimental validation. The framework is a straightforward assembly of existing components without rigorous justification or convincing empirical evidence. Given the ICLR standard, the contribution does not meet the threshold for acceptance.

MY FINAL SCORE: 3</score>
MY FINAL DECISION: Reject</decision>
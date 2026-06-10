Now I'll produce the final consolidated review.

---

## Summary

The paper proposes a framework for injecting human knowledge into MARL communication using a "text-to-mask" model that maps textual object descriptions to binary masks over agent observations. The communication policy selects which features to discuss (via Bernoulli variables over textual terms), while the encoding of masked features is learned via RL with a behavioral cloning (BC) constraint from a rule-based "human strategy." Experiments on two custom environments compare the hybrid method against no-comm, human-strategy-only, and dense-comm (unmasked observations) baselines.

## Strengths

- **Formal text-to-mask abstraction**: The paper defines a clean interface (Section 4.1) $\mathcal{F}: \mathcal{T} \times O \rightarrow \{0,1\}^{|O|}$ that maps textual terms to observation-space masks. This creates a principled way to inject human object-level priors without requiring the human to specify the encoding — the agent learns that via RL. The abstraction is domain-agnostic and could be extended to other settings. This goes beyond prior approaches like DIAL (which uses learned continuous vectors) and attention-based methods (which learn to filter end-to-end) by creating a structured human-agent interface.

- **Environment controls for implicit communication**: The environments are explicitly designed (Section 3, lines 33–35) to minimize implicit communication by swapping agent observations and removing direct connections between the reward and decentralized observations. This is a stronger experimental design than typical MARL benchmarks and ensures that measured performance differences reflect communication quality rather than coincidental coordination.

## Weaknesses

### Fatal
None.

### Major

- **Statistically insufficient evaluation**. The Coordinate Images experiment uses **only 2 random seeds** (line 148). In MARL, variance across seeds is a well-documented problem, and 5–10 seeds is the accepted minimum in the field. Without confidence intervals or error bars, the reader cannot determine whether the reported advantage of 'hybrid' over 'human-strategy' (which also performs well) is meaningful or a lucky draw. Even worse, the Coordinate environment (Section 5.1) does not state how many seeds were used, and its results are never described in the text — the only reference is "Similarly to Fig. 5" (line 148) with no description of what Fig. 5 shows, making that half of the evaluation uninterpretable.

- **The 'dense comm' baseline fails without explanation, undermining the experimental setup**. The dense-comm baseline — which broadcasts unmasked observations and is described as a variant of DIAL (line 94) — performs at the level of a random policy in Coordinate Images (Fig. 7). The paper itself calls this "surprising" (line 148) but provides no investigation. Possible explanations (encoder capacity mismatch, improper implementation, environment design that penalizes dense input) are not explored. Since this is the paper's only learned-communication baseline, its unexplained failure means the main result (hybrid > dense comm) cannot be cleanly attributed to the proposed method's strengths rather than a broken baseline.

- **No ablation isolating the contribution of the human prior**. The 'hybrid' method uses both the human-strategy BC loss and RL. Without an ablation that runs the same architecture RL-only (no BC loss) on masked observations — which is a natural and cheap experiment — the paper cannot show that the human prior provides benefit over learning to select features from scratch. The 'human-strategy' baseline already achieves good performance (Fig. 7), further blurring whether the RL component adds meaningful value over the rule.

- **No sensitivity analysis for key hyperparameters**. The BC weight $\beta$ and the communication penalty $\alpha$ (line 87) are central to the method but receive no ablation or sensitivity study. The sequential batch-by-batch training (line 87) is described as "crucial for convergence" but is not compared against joint training or analyzed in any way.

### Minor

- **Missing promised definition**. The introduction (line 12) states: "We formulate a proper definition for such problems and provide further insights at Section 3." Section 3 contains only a standard DEC-POMDP formulation and discussion of implicit communication — no definition of "complex" vs. "simple" problems. This is a broken narrative promise.

- **Framing overreach relative to implementation**. The abstract mentions "human feedback" and the title invokes "human-like communication strategies," but the method uses a hand-coded rule (e.g., "communicate all objects in the other player's forehead") and a fixed feature-selection mask (line 146: "the text-to-mask model is trivial here"). There is no NLP, no language model, no actual human feedback, and no grounding of communication signals to natural language. The implementation is transparently described, but the framing inflates expectations beyond what is delivered.

### Trivial
None.

## Nice-to-Haves

- Comparing against a learned communication baseline that demonstrably works (e.g., attention-based communication from Jiang & Lu 2018, or autoencoder-based from Lin et al. 2021) would strengthen the claim that human knowledge injection helps beyond existing learned approaches.
- Using a human strategy that is useful but incomplete (not essentially solving the communication problem) would more convincingly demonstrate the RL component's contribution. In Coordinate Images, the human rule ("communicate objects in the other player's forehead") is so close to optimal that the human-strategy baseline already succeeds, leaving little room for RL to add value.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No code release / reproducibility details"** (harsh critic): Removed per hard rule — reproducibility nitpicks about undisclosed hyperparameters and trivial implementation details are not author errors.
- **"No human data" / "should use real human demonstrations"** (harsh critic): Removed — the paper explicitly argues that collecting human demonstrations is impractical (line 49) and proposes an indirect alternative. Demanding real human data is scope creep.
- **"Interpretability via observable communication subjects"** (strength finder): Removed as too weak — the qualitative walkthrough of a single simple-environment trajectory (Section 6) does not constitute evidence of interpretability by any rigorous standard, and this conflicts with the verified weakness that the interpretability analysis is non-rigorous.
- **"Missing baselines from the literature (attention-based, autoencoder-based)"** (harsh critic): Partially removed — the paper does include a DIAL variant (dense comm) as a learned communication baseline. The real problem is that this baseline fails inexplicably, not that it is absent. The request for additional baselines is softened to a nice-to-have.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the text-to-mask abstraction is a novel architectural idea with potential, but the experimental evaluation is not at the level needed to support the paper's claims for a top venue. The core issue is not a flaw in the idea but a gap between the ambition of the claims and the thinness of the evidence.

## Suggestions

1. Run all experiments with at least 10 random seeds and report means with confidence intervals or standard deviations.
2. Diagnose why dense-comm fails — or replace it with a properly tuned learned communication baseline.
3. Add the critical ablation: train the same architecture with masking but WITHOUT the BC loss, to isolate the value of the human prior.
4. Report the Coordinate environment results with proper statistical detail, or remove it if incomplete.
5. Deliver the promised definition of "complex" problems in Section 3, or remove the reference to it.
6. Adjust the framing ("human feedback," "human-like communication") to match what is implemented: feature-selection masks with rule-based priors.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
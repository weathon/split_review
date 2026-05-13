Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes a collaborative multi-agent navigation task where a Tourist agent with local visual observations and a Guide agent with global environment knowledge learn to communicate via multi-turn emergent language dialogues, trained end-to-end with REINFORCE and auxiliary pre-training tasks. The system is evaluated on R2R and CVDN benchmarks (using only the simulator, discarding natural language), with ablations on vocabulary size, message length, and dialogue frequency, and the authors claim the emergent language aligns with visual surroundings and dialogue goals.

## Strengths

- **Novel task formulation extending emergent communication to dynamic, multi-turn settings with real-world simulator**: The paper moves beyond the dominant single-turn, static-environment paradigm in emergent communication by introducing multi-turn dialogue in a navigation task with the Matterport3D simulator. This is a meaningful and well-motivated extension of prior EC work (Section 3, Section 1).
- **Systematic ablation studies on key design parameters**: Tables 3–4 and Figure 3 provide informative empirical findings: performance scales with dialogue frequency, peaks at moderate vocabulary/message sizes, and declines at large action spaces—honest and useful negative results for the community (Sections 5.4).
- **Decomposed pre-training strategy**: The two auxiliary tasks (localization and movement) that bootstrap RL training from sparse rewards are a pragmatically sound design that stabilizes otherwise difficult end-to-end training (Section 4.5).

## Weaknesses

### Fatal
None.

### Major

- **Invalid comparison framing with VLN baselines**: The paper claims "performance comparable to those of the established approach" (Section 6), comparing Table 1/Table 2 results against VLN baselines (Seq2Seq, Speaker, etc.). However, the tasks are fundamentally different: VLN baselines solve "navigate from a human instruction" where the instruction is provided once and is potentially ambiguous, while the proposed system gives the Guide full graph knowledge (all node images, connectivity, shortest paths to target—Equation 3 explicitly computes `ShortestPath(E, pos_i, tgt)`) and allows multi-turn interactive dialogue. The Guide is an oracle with perfect environmental knowledge and planning capability, making the comparison structurally unfair in the proposed method's favor. Navigation success under such strong oracle conditions does not validate emergent language quality. The ablation with no communication (message length = 0 in Table 3) partially addresses this but is insufficient—what is needed is a controlled ablation holding oracle knowledge constant while varying the communication channel (e.g., continuous vectors vs. discrete tokens).

- **"High alignment" claim between emergent language and visual/semantic content is unpersuasive**: The abstract and conclusion state that "emergent messages highly align with both surroundings and dialogue goals." The sole evidence is Figure 4(a), a t-SNE visualization showing "similar distributions" between observation and message vectors, and anecdotal observations about "similar visual patterns sharing similar symbol n-grams." There is no quantitative alignment metric (e.g., mutual information, probing accuracy, cluster purity), no comparison against a random-language baseline, and no analysis mapping specific symbols to semantic content. t-SNE can produce superficially similar distributions from very different underlying structures. Without quantitative grounding analysis, the core semantic alignment claim is unsupported (Section 5.5).

- **Unexplained val_unseen > val_seen anomaly on CVDN**: On CVDN (discussed in Section 5.3), the proposed method achieves higher Goal Progress and Adapted Goal Progress on val_unseen than val_seen (the paper itself notes "lower results in the val seen ones"). This pattern is atypical—in virtually all VLN work, val_seen outperforms val_unseen because the unseen environments are genuinely harder. The paper claims this "signifies that the emergent language-based dialogue system generalizes eminently on unseen scenes," but this interpretation is unfounded without investigating potential causes (e.g., data distribution artifacts, overfitting to specific training scenes, or noise). An anomaly this unusual demands investigation, not celebration.

### Minor

- **Variable-length experiment undermines efficiency claim**: When agents are allowed variable-length messages (up to 20 symbols), they "greedily generate messages with the full 20 symbols" despite a length penalty (Section 5.4). This suggests the emergent language has not learned efficient communication, which contradicts the framing that agents learn concise task-oriented dialogue. The authors note this but defer investigation to future work.

- **Ambiguity between pre-training and joint training**: Section 4.5 describes auxiliary tasks as "pre-training," but the combined `L_nav` loss (Equation 173) appears to integrate localization and movement rewards, suggesting joint training. Whether these are pre-training only or jointly optimized matters for understanding the training dynamics.

### Trivial
None.

## Nice-to-Haves

- **Probing experiments**: Train classifiers to predict Tourist location from Guide utterances, or intended actions from Tourist utterances—with quantitative accuracy metrics. This would directly test whether emergent language transmits semantically meaningful information.
- **Controlled communication ablation**: Compare discrete emergent language against continuous-vector communication and random-token communication, holding the Guide's oracle knowledge constant, to isolate the contribution of emergent language.
- **Failure mode decomposition**: When navigation fails, decompose into Guide-localization failure, communication failure, or Tourist-execution failure to reveal where the system breaks down.
- **Multiple random seeds**: Report results with standard deviations across seeds, given the known high variance of REINFORCE training.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic's claim about "not yet released" or unverifiable models/benchmarks**: Not applicable—the paper cites standard benchmarks (R2R, CVDN, Matterport3D). Removed per hard rules.
- **Strength Finder's "No human annotations" as a strength**: The "no human annotation" property is a feature of the task setup, not a demonstrated strength of the method. The paper's results don't clearly show the method achieves comparable results *because* it avoids human annotations—the oracle Guide's full graph knowledge more than compensates. Removed as conflicting with the verified weakness about the invalid comparison.
- **Strength Finder's "lowest NE on R2R val unseen" and "highest GP on CVDN val unseen"**: These claims about strong generalization to unseen environments are undermined by the structural unfairness of the comparison (oracle Guide with full graph access vs. VLN models with single human instructions) and the unexplained val_unseen > val_seen anomaly. Removed as conflicting with verified weaknesses.
- **Harsh Critic's complaint about "missing proofs in appendix"**: Removed per hard rules (parser strips appendices).
- **Harsh Critic's complaint about "unspecified threshold ρ"**: This is a minor hyperparameter detail, not a reproducibility barrier. Removed as a nitpick.
- **Harsh Critic's suggestion about "missing variance and reproducibility"**: This is a nice-to-have, not a core flaw. Standard in the field for RL papers to report single runs on benchmarks. Moved to nice-to-haves.

## Novel Insights

The variable-length message experiment revealing that agents fill the maximum allowed length despite penalties is a quietly important negative result about emergent communication efficiency: it suggests that when action spaces grow, learned protocols trend toward using maximum available capacity rather than compressing information, calling into question whether emergent languages naturally develop the efficiency properties of human language. This insight is underemphasized in the paper but has implications for the broader EC community.

## Suggestions

- Add a controlled ablation that replaces the discrete emergent language with a continuous communication channel (of similar dimensionality) while keeping all other experimental conditions identical. This single experiment would directly measure whether discrete language provides any advantage and substantiate (or undermine) the core contribution claim.
- Replace the t-SNE-based alignment analysis with quantitative probing experiments (e.g., linear classifiers predicting ground-truth location from message embeddings) and report accuracy/F1 scores compared to random baselines. This is straightforward to implement and would transform the alignment claim from anecdotal to evidential.
- Investigate the val_unseen > val_seen CVDN anomaly: report per-scene breakdowns, check whether specific unseen scenes happen to be structurally simpler, and compare the distribution of goal distances across splits.

---

**Evaluation on axes:**
- **Originality**: Moderate. Extending emergent communication to multi-turn, dynamic settings with a real simulator is a genuine contribution, though the RL framework and Transformer architecture are standard.
- **Importance of research question**: Reasonable. Multi-turn emergent communication in embodied settings is an important open problem.
- **Whether claims are well supported**: Weak. The two central claims—comparable performance to VLN methods and high alignment of emergent language—are undermined by an apples-to-oranges comparison and anecdotal evidence respectively.
- **Soundness of experiments**: Moderate ablations are present and informative, but lack the controlled experiment that would isolate emergent language's contribution from oracle knowledge.
- **Clarity of writing**: Adequate with some dense notation.
- **Value to research community**: The task formulation and ablation findings have value, but the unsupported claims limit the impact.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
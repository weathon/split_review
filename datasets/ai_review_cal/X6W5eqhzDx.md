- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3
Now I have all the information needed to produce the consolidated review. Let me cross-reference the critic's claims against the paper and produce the final assessment.

---

## Summary

This paper introduces the concept of *reachability* for multi-task reinforcement learning, formally distinguishing "reachable tasks" (whose start states can be encountered during training) from "unreachable tasks." The authors argue that improved generalization from exploration is driven by training on more reachable tasks (start states) rather than by exploring more states overall. They propose **Explore-Go**, a simple method that prepends a pure-exploration phase to each training episode, using the terminal state of that phase as the episode's effective start state. Experiments in Four Rooms (with SAC, DQN, PPO) and DeepMind Control Suite (state- and image-based) show that Explore-Go improves test performance, and a controlled comparison with Temporally Equalised Exploration (TEE) shows that Explore-Go outperforms a method that explores more states but does not structure that exploration around start-state diversity.

---

## Strengths

1. **Clear conceptual framing of reachability.** Definition 1 (Section 3.1) formally distinguishes reachable from unreachable tasks based on whether start states belong to the reachable state set during training. This provides a principled lens for understanding both *why* exploration can help generalization (as data augmentation on reachable tasks) and *why* continuous exploration (TEE) can be suboptimal even when it discovers more states.

2. **Empirical demonstration that Explore-Go outperforms a method with more state coverage.** The TEE comparison (Figures 4–5 in the paper) shows that DQN+TEE explores a larger fraction of the state-action space, maintains higher state diversity in the buffer, and learns optimal actions in more reachable *states* — yet DQN+Explore-Go achieves significantly higher generalization on both reachable and unreachable test sets. This directly supports the paper's central claim about the importance of *when* exploration occurs rather than *how much*.

3. **Versatility across on-policy and off-policy algorithms.** Section 5.1 demonstrates that Explore-Go improves unreachable test performance when combined with SAC, DQN, and PPO in Four Rooms (Figure 3), while training performance remains largely unaffected. This shows the method is not tied to a specific algorithmic family.

4. **Scalability to continuous control with both state and image observations.** Section 5.3 shows that Explore-Go improves test performance on Finger Turn and Reacher from DMC with state-based observations (Figure 6) and with image-based observations when combined with RAD (Figure 7), demonstrating applicability beyond discrete gridworlds.

---

## Weaknesses

### Fatal
None.

### Major

- **The central causal claim is not fully isolated from a confound.** The paper argues that generalization improvement comes from training on *more reachable tasks* rather than from more exploration or optimality in more states. The key evidence is the Explore-Go vs. TEE comparison, but the two methods differ along **two axes simultaneously**: (a) the number of reachable tasks trained on, and (b) the quality of the targets used for learning. The paper itself acknowledges in Section 3 (lines 107–109) that exploratory trajectories can provide "poor target estimates" and that Explore-Go's use of on-policy rollouts from explored start states avoids this problem. Because TEE collects high-exploration trajectories (high-ε workers take many random actions) and uses that data for learning, the comparison conflates "more reachable tasks" with "cleaner targets." A cleaner isolation experiment — e.g., comparing Explore-Go to a TEE variant that also resets to explored states before doing on-policy rollouts, or directly measuring the fraction of start states solved optimally over time — would substantially strengthen support for the mechanism claim. As written, the paper's evidence supports the method's effectiveness but does not fully establish the specific causal mechanism it proposes.

### Minor

- **The DMC experiments do not exhibit a generalization gap, weakening the generalization narrative.** The paper acknowledges (line 189) that "there appears to be no significant generalisation gap between training and testing in either environment." If train and test performance are essentially the same, the improvement shown is an overall performance improvement rather than specifically improved *generalization* to held-out tasks. The paper frames itself around the ZSPT generalization problem (title, abstract, introduction), yet the DMC results do not demonstrate a generalization gap that Explore-Go closes. The results still show that Explore-Go improves performance and scales to continuous control, but the claim that this demonstrates a generalization benefit is ambiguous in these environments. The paper should either select environments with a clear gap, or more prominently reframe these results as demonstrating scalability rather than generalization.

- **The operationalization of reachability in Four Rooms may not perfectly align with the formal definition.** The paper defines reachable tasks in Four Rooms as those where "both the positions of the doorways and the goal location are the same as at least one training task" (line 130). However, the formal definition (Definition 1) defines reachability based on whether the start state belongs to the reachable state set $S_r$, which depends on the full transition dynamics. The paper should clarify why this proxy matches the formal definition, or explicitly treat it as an approximation.

- **No dedicated limitations or failure-mode discussion.** The paper does not include a limitations section. Explore-Go uses uniform random actions as its pure exploration policy, which may fail in environments with sparse reward or hard-exploration structure where random actions do not effectively cover the state space. The assumption that the state representation factors out task-specific features (line 40) may not hold in all environments. Adding a limitations paragraph would strengthen the paper.

### Trivial
- None that survive filtering after cross-checking with the paper.

---

## Nice-to-Haves

- A direct measurement of "number of reachable tasks solved optimally" (i.e., the fraction of start states for which the agent achieves near-optimal return), tracked over time, would directly support the causal claim.
- An empirical comparison with the reset controller approach of Zhu et al. (2020) would help contextualize the contribution, though the paper already discusses this work in the related work section.
- A discussion of alternatives to uniform random exploration (e.g., count-based or curiosity-driven exploration) for environments where random actions are insufficient.

---

## Removed Points

These points were identified by reviewers but removed after cross-checking against the paper:

- **"No statistical significance tests"** — Removed. RL papers standardly report confidence intervals (which this paper does); demanding p-values is a non-standard requirement for this community.
- **"Easy variant names not explained"** — Removed. "Finger Turn Easy" and "Reacher Easy" are standard DMC environment names, not author-chosen difficulty levels.
- **"Illustrative example mapping to formal definitions not fully tight"** — Removed. The criticism is vague and lacks a specific concrete issue to anchor to.
- **"Missing comparison to reset controllers empirically"** — Moved to Nice-to-Have. The paper discusses Zhu et al. in related work; an empirical comparison would strengthen but is not required.
- **"Missing appendix content"** — Removed per instructions (parser strips appendices; they exist in the original submission).
- **"TEE comparison confounded by different effective episode horizons"** — Removed. The episode-length difference is a design feature of the methods being compared, not an uncontrolled confound.
- **"Inability to independently verify cited methods"** — Removed per hard rule: all cited references are assumed to exist.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface any observation about the paper that the paper itself does not already make or imply.

---

## Suggestions

1. **Isolate the mechanism experimentally.** The most valuable addition would be a comparison between Explore-Go and a variant of TEE that also resets to explored states at episode start before doing on-policy rollouts (or equivalently, discards the exploratory data and only uses the on-policy portion for learning). If this TEE variant matches Explore-Go, the "more reachable tasks" mechanism is supported; if not, target quality is a dominant factor.

2. **Directly measure "tasks solved optimally."** In Four Rooms, track the fraction of distinct start states for which the agent achieves near-optimal return. Show that Explore-Go solves more distinct start states optimally despite visiting fewer total states than TEE.

3. **Acknowledge the DMC limitation more prominently.** Explicitly state that the DMC experiments demonstrate scalability and performance improvement, but that the observed benefit may reflect overall improvement rather than specifically improved generalization (since no gap exists between train and test).

4. **Add a limitations section** discussing when uniform random exploration may fail, the scope of the state-representation assumption, and potential failure modes of the method.

---

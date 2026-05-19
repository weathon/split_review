## Summary
The paper introduces OC-STORM, an object-centric model-based reinforcement learning (MBRL) pipeline that integrates a frozen foundation vision model (Cutie) to extract compact object features from raw observations. By conditioning the world model on these object vectors alongside resized visual inputs, the method aims to mitigate the limitations of traditional pixel-space reconstruction losses (e.g., L2 loss), which often prioritize large background areas and discard decision-critical details in visually complex environments. The authors evaluate OC-STORM on the Atari 100k benchmark and the visually complex game Hollow Knight, demonstrating improved sample efficiency and performance over the baseline STORM. Ablation studies show that compact vector representations outperform binary masks, and the method achieves strong results without requiring internal game states or extensive labeling.

## Strengths
1. **Clear Problem Identification:** The paper correctly identifies a critical bottleneck in pixel-based MBRL: L2 reconstruction losses prioritize large background areas, causing latent spaces to discard small, decision-relevant objects in visually complex environments.
2. **Effective Integration of Foundation Models:** Leveraging a frozen, pre-trained video object segmentation model (Cutie) to extract compact, semantically rich object vectors is a practical and innovative approach that decouples perception learning from control learning.
3. **Strong Empirical Validation:** The method demonstrates consistent improvements over STORM on Atari 100k and achieves impressive sample efficiency on the visually complex Hollow Knight benchmark, validating the utility of object-centric representations in non-trivial settings.
4. **Insightful Ablation Studies:** The comparison between compact vectors and binary masks provides clear mechanistic evidence that semantic compression outperforms spatial occupancy masks for world modeling, strengthening the paper's core contribution.

## Weaknesses
1. **Circular Reasoning in Atari Categorization:** The post-hoc grouping of Atari games into "object-representable" versus "background-dependent" risks circular reasoning. Defining success by the environments where the method naturally fits weakens the generalizability claim. This should be reframed as a boundary condition for object-centric MBRL.
2. **Insufficient Quantification of Sample Efficiency:** While the paper claims OC-STORM "converges significantly faster" on Hollow Knight, it lacks explicit quantitative metrics (e.g., steps to reach 50% win rate) and direct references to training curves in the main text. This makes it harder to assess the magnitude of the sample efficiency gains.
3. **Limited Discussion on Duplication Mitigation:** The limitation regarding duplicated instances (e.g., Mantis Lords) is well-identified but deferred entirely to future work. Proposing a concrete mitigation (e.g., spatial pooling or instance-ID tokens) would demonstrate a clearer path forward and increase the paper's impact.
4. **Overclaiming in Contribution Statement:** The claim of being the "first to successfully adopt object-centric learning on Atari and Hollow Knight without relying on an extensive number of labels" is high-risk without precise scoping. Emphasizing the pipeline's practical value and sample efficiency gains is more defensible.

## Key Issues
1. **Boundary Condition Framing:** The Atari categorization (Table 2) currently reads as a success metric rather than a methodological boundary. The paper needs to explicitly discuss why background-dependent games (e.g., CrazyClimber, Gopher) require spatial layout information that compact object vectors cannot capture, and how this limits the generalizability of OC-STORM.
2. **Sample Efficiency Quantification:** The claim of faster convergence on Hollow Knight lacks quantitative backing in the main text. Without explicit metrics (e.g., steps to 50% win rate) or direct references to Appendix D.6, readers cannot fully assess the practical sample efficiency gains.
3. **Duplication Handling Strategy:** The inability to handle duplicated instances is a significant limitation for real-world deployment. Deferring this entirely to future work weakens the method's robustness claims. A concrete mitigation strategy should be proposed to show scalability.

## Actionable Suggestions
1. **Reframe Atari Categorization:** Rewrite the discussion around Table 2 to explicitly frame the "background-dependent" category as a boundary condition. Add a sentence explaining that continuous spatial layouts require raw visual context, which compact vectors cannot capture, and discuss how hybrid representations could address this.
2. **Quantify Hollow Knight Gains:** In Section 4.2, add explicit quantitative metrics for sample efficiency (e.g., "OC-STORM reaches 50% win rate on Mage Lord in X steps, compared to Y steps for STORM") and directly reference the training curves in Appendix D.6 to substantiate the "converges significantly faster" claim.
3. **Propose Duplication Mitigation:** In the Limitations section, propose a concrete mitigation for duplicated instances, such as augmenting object vectors with explicit spatial coordinates or instance-ID tokens. This demonstrates a clear path forward and increases the paper's impact.
4. **Tighten Contribution Statement:** Replace the "first to successfully adopt" claim with a more defensible emphasis on the pipeline's practical value, sample efficiency gains, and the ablation finding that compact vectors outperform binary masks.

## Storyline Options + Writing Outlines
**Abstract Outline:**
S1 (Problem): Deep RL struggles with sample efficiency in visually complex environments where small, dynamic elements dictate optimal actions.
S2 (Gap): Traditional MBRL relies on pixel-space reconstruction (e.g., L2 loss), which prioritizes large background areas and discards decision-critical details.
S3 (Method): We propose OC-STORM, an object-centric MBRL pipeline that integrates a frozen foundation vision model (Cutie) to extract compact, decision-relevant object features.
S4 (Mechanism): By conditioning the world model on these object vectors alongside raw observations, OC-STORM focuses imagination on key dynamics and decouples perception from control.
S5 (Result): We demonstrate significant sample efficiency gains over STORM on Atari 100k and strong performance on Hollow Knight, without requiring internal game states or extensive labeling.

**Introduction Outline:**
P1 (Big Picture): DRL's success vs. sample efficiency bottleneck in real-world/complex visual settings.
P2 (Gap): MBRL offers a solution via imagination, but L2 reconstruction losses fail to capture small, decision-relevant targets in cluttered scenes, leading to latent space misalignment.
P3 (Solution): Foundation vision models (e.g., Cutie) provide robust, semantic object representations independent of background complexity.
P4 (Method): OC-STORM integrates these compact vectors into a transformer-based world model, enabling focused dynamics prediction.
P5 (Evidence): Experiments on Atari 100k and Hollow Knight show superior sample efficiency and performance, with ablations confirming vectors outperform masks.
P6 (Contribution): Summary of pipeline, empirical validation, and practical few-shot annotation protocol.

## Priority Revision Plan
**P0 (Critical - Claim & Evidence Alignment):**
- Reframe Atari categorization (Table 2) as a boundary condition rather than a success metric. Explicitly discuss why background-dependent games require spatial layout information.
- Quantify Hollow Knight sample efficiency gains in Section 4.2 with explicit metrics (e.g., steps to 50% win rate) and reference Appendix D.6.
- Tighten the contribution statement to avoid high-risk "first" claims; emphasize practical value and vector-vs-mask ablation findings.

**P1 (Major - Methodological Rigor):**
- Propose a concrete mitigation for duplicated instances in the Limitations section (e.g., spatial pooling or instance-ID tokens) to demonstrate scalability.
- Strengthen the mechanistic explanation for why vectors outperform masks in Section 5.2 (e.g., downsampling artifacts vs. semantic compression).

**P2 (Minor - Writing & Presentation):**
- Correct typo "Hollow Kight" in Section 4.2.
- Improve transition between abstract problem statement and proposed solution by explicitly linking L2 loss limitations to latent space misalignment.
- Ensure conclusion explicitly reiterates key empirical findings and practical implications.

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | OC-STORM improves sample efficiency over STORM | Atari 100k (26 games), 5 seeds | HNS mean/median | Outperforms STORM on 18/26 tasks | C2 | Post-hoc categorization risks circularity |
| E2 | OC-STORM handles visually complex environments | Hollow Knight (6 bosses), 3 seeds | Episode return, Win Rate | Strong performance, faster convergence | C2 | Lacks explicit sample efficiency metrics |
| E3 | Compact vectors outperform binary masks | Atari Boxing/Pong, 5 seeds | Training returns | Vectors consistently outperform masks | C3 | Mechanistic explanation could be sharper |
| E4 | Object representation completeness | Atari Boxing decoder | Reconstruction quality | Features capture state/position | C1 | Qualitative only |

**Research-Theme Gap Diagnosis:**
The core claim of improved sample efficiency in visually complex environments is well-supported, but the quantification of *how much* efficiency is gained (e.g., steps to convergence) is missing in the main text. Additionally, the boundary conditions for object-centric MBRL (background-dependent games) need clearer framing.

**Proposed Research Experiments:**
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|
| C2 (Sample Efficiency) | OC-STORM reaches competitive win rates faster than STORM | Plot training curves for Hollow Knight bosses | STORM, OC-STORM | Steps to 50% WR | Clear delta in convergence steps | Low (existing data) | Quantifies efficiency gains |
| C1 (Boundary Conditions) | Hybrid representations improve background-dependent games | Add spatial layout token to OC-STORM | OC-STORM, STORM | HNS on CrazyClimber/Gopher | Performance parity or improvement | Medium | Clarifies method limits |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 6.5/10
The paper presents a practical and well-motivated pipeline for object-centric MBRL, with strong empirical validation on Atari and Hollow Knight. The integration of foundation vision models to decouple perception from control is a valuable contribution. However, the score is moderated by the circular framing of Atari categorization, lack of explicit sample efficiency quantification in the main text, and high-risk "first" claims in the contribution statement. Addressing these issues would significantly strengthen the paper's defensibility and impact.

Post-Revision Target: [7.5, 8.5]/10
If the authors reframe the Atari categorization as a boundary condition, explicitly quantify sample efficiency gains, and propose concrete mitigations for duplicated instances, the paper will achieve strong claim-evidence alignment and clearer methodological positioning, warranting a higher score.
Now I have all the information I need. Let me synthesize the review.

## Summary

This paper identifies a practical gap in federated learning: personalized models (PMs) perform well on local test data but poorly on test data from other clients' distributions. The authors formulate Selective FL (SFL) to formally bridge GFL and PFL, then propose HPFL—a two-stage framework where clients learn a shared backbone (via FedAvg), train per-client plug-in modules (linear classifiers on the frozen backbone), and at test time select the most suitable plug-in based on feature similarity. Experiments on four datasets and three architectures show HPFL substantially outperforms existing FL methods on the GFL-PM task (e.g., 79.0% vs. 65.7% on CIFAR-10 with Dir(0.1)), while remaining competitive in the standard PFL setting.

## Strengths

1. **Clear empirical superiority on the GFL-PM task across multiple benchmarks.** Table 2 shows HPFL outperforms all baselines (FedAvg, FedPer, FedRep, PerFedMask, FedRoD, FedTHE) on GFL-PM accuracy across four datasets and two heterogeneity levels, often by a large margin (e.g., 79.0% vs. FedRoD's 65.7% on CIFAR-10 Dir(0.1); 70.9% vs. 66.5% on CIFAR-100 Dir(0.1)). This directly supports the paper's central claim.

2. **Architecture-agnostic design validated across three network families.** Table 3 confirms HPFL works with ResNet-18, MobileNet, and a simple CNN, consistently outperforming baselines on GFL-PM. This shows the framework is not tied to a specific architecture.

3. **Robustness to privacy-preserving noise in the selection phase.** Table 4 shows that adding Gaussian noise to shared features (κ from 1 to 10) causes negligible accuracy loss (≤0.8% on CIFAR-10, ≤0.4% on Fashion-MNIST), demonstrating the selection mechanism works even under substantial noise.

4. **Practical problem formulation.** The paper correctly identifies a real-world limitation of PFL—the inability to handle test data from other distributions—and provides a clean architectural decomposition (backbone + plug-ins + selection) to address it. The idea is intuitive and well-motivated.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation of selection accuracy.** The paper's core mechanism is plug-in selection, and Section 5.3 is devoted to studying it. Yet the analysis relies entirely on heatmaps (Figures 3, 4) with no numerical metric such as top-1/top-k selection accuracy (what fraction of test samples from client *i* are assigned client *i*'s plug-in?). The paper claims "accurate selection algorithm" (abstract) and "precise plug-in selection" (Section 5.2), but these claims are unsupported by any quantitative measurement. Without this, one cannot tell whether performance gains come from good selection or from having many plug-ins such that even random selection would help. The heatmaps in the parsed version reference anchors ("green anchor") that are not visible in the text, and the description is purely qualitative. This is the most significant gap in the evaluation.

   *The paper partially acknowledges this in the Limitations section ("our proposed plug-in selection methods select suboptimal plug-ins in some circumstances"), but acknowledging the problem does not substitute for providing the missing metric.*

2. **Unsupported privacy claims.** Section 4.3 states that sharing noised features "testif[ies] sharing the noised feature stays safe from model inversion attack." Section 5.2 claims "Efforts to protect privacy is not contradictory to the performance of HPFL" and Table 4 shows noise does not degrade accuracy. However, no formal privacy analysis (differential privacy, reconstruction attack evaluation, or even a citation to an attack study applied to this setting) is provided. Showing that noise does not hurt accuracy does not demonstrate that the protocol is actually private. Sharing intermediate features (even noisy ones) is known to leak information; the paper's claim of safety is unsubstantiated.

### Minor

3. **Overclaimed theoretical contribution.** Section 3 formulates SFL with two theorems that are conceptually straightforward. Theorem 3.1 states that the optimal PFL loss lower-bounds the GFL-PM loss under Eq. 4 (each client's PM outperforms others on its own data)—this follows directly from averaging over the inequality in Eq. 4. Theorem 3.2 states that perfect selection of the correct PM recovers this lower bound—essentially a tautology about an oracle selector. The paper presents these as a "new problem" that "bridges" GFL and PFL, but the theorems add no analytical machinery, trade-off analysis, or non-trivial insight beyond what the problem statement already implies. The practical HPFL framework is the real contribution; the theoretical section would be more honestly framed as a formal description of the desideratum rather than a novel theoretical result.

4. **Incomplete FCL experiment description.** Section 5.4 and Table 5 report FCL results but do not explain the experimental setup: what are "Group 1, Group 2, Group 3"? How many clients per group? Is the backbone frozen or updated when new groups join? If the backbone is updated, how does HPFL avoid feature shift that would invalidate previously learned plug-ins? As presented, the FCL results are suggestive but cannot be properly evaluated or reproduced.

5. **Notation mismatch between theory and practice.** In Section 3.4, Eq. 5 defines the SFL objective as minimizing over ℋ (auxiliary information), but ℋ is never formally defined as an optimization variable. In practice (Section 4.3), ℋ_m becomes the noised feature centroid ĥ_m, which is a stored byproduct of plug-in training—not something optimized over. The theoretical framing implies a selection mechanism is learned, while the practical method uses a fixed distance-based rule. This disconnect is not addressed.

### Trivial
None.

## Nice-to-Haves

- **Add a k-NN baseline using backbone features.** A simple non-parametric classifier on the frozen backbone features would isolate whether HPFL's per-client plug-in training (learning linear heads) adds value beyond using the backbone representations directly with a distance-based decision rule. This would strengthen the claim that the plug-in stage itself is beneficial.

- **Add an oracle selection baseline.** Reporting the accuracy achieved by always selecting the correct plug-in (i.e., an oracle selector) would establish the upper bound of the framework and quantify the remaining headroom for improving selection.

- **Clarify the plug-in architecture explicitly.** The paper implies the default plug-in is a single linear layer (since deeper plug-ins degrade performance), but this is never stated. Explicitly specifying this and analyzing whether performance loss from deeper plug-ins is due to selection difficulty or overfitting would strengthen Section 5.3.

- **Quantify computational/communication overhead.** HPFL requires storing all plug-ins on the server and transmitting test features for selection. A brief discussion of these costs (e.g., memory footprint for M=10,000 clients, feature upload bandwidth per inference) would help practitioners assess deployability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Weak baselines for the GFL-PM setting" (critic's framing):** The critic suggests the comparison is unfair because PFL methods are not designed for GFL-PM. However, the paper's goal is to show that existing methods fail at this task, which is the motivation for HPFL. Including PFL baselines is appropriate to demonstrate the gap. The critic's specific suggestions (k-NN, oracle) are valid additions but the existing baseline set is not a weakness. *Moved to Nice-to-Haves.*

- **Criticisms about unverifiable claims regarding Dir(0.05) results and M=100 scalability:** The critic notes these claims cannot be verified from the parsed text because the relevant table entries are embedded in images. This is a parser artifact, not a paper problem; the original submission contains these numbers.

- **Criticism about missing CKA/SVCCA results:** The paper notes these are deferred due to page limitations. *Removed per rule about missing appendix content.*

## Novel Insights

The reviews surface a productive tension: the paper's practical contribution (HPFL) is genuinely strong—clean architectural decomposition, large empirical gains, architecture-agnostic—but its theoretical framing and evaluation methodology have gaps that prevent the reader from fully trusting the mechanism. The most interesting unresolved question is whether HPFL's gains truly come from *correct* plug-in selection (as claimed) or from a softer effect: having access to an ensemble of specialized classifiers on frozen features, where even imperfect selection outperforms any single model. The absence of a quantitative selection metric means this question cannot be answered from the paper as presented. A second insight from combining the reviews is that the privacy discussion sits awkwardly between two valid concerns—the paper is right that noise robustness is useful, but wrong to assert safety without analysis—and this section would benefit from either formal guarantees or honest hedging.

## Suggestions

1. **Add quantitative selection accuracy metrics** to Section 5.3: report the fraction of test samples from each client that are assigned the correct plug-in (diagonal entries in a confusion matrix), both with and without noise. This is the single most important addition to validate the core mechanism.

2. **Either provide a formal privacy analysis or soften the privacy claims.** If the paper can offer differential privacy guarantees (by calibrating noise to the sensitivity of the feature centroids), include them. Otherwise, replace phrases like "stays safe from model inversion attack" with empirically grounded statements like "noise up to κ=X does not degrade accuracy" and acknowledge that privacy is not formally proven.

3. **Acknowledge the simplicity of the theoretical results** and reframe SFL as a problem formalization/desideratum rather than a novel theoretical contribution. This would align the paper's claims with what it actually delivers.

4. **Describe the FCL experimental setup** in sufficient detail (group composition, backbone update protocol, per-group metrics) so the results can be interpreted.

5. **Include a k-NN baseline** using backbone features (no plug-in training) to ablate the value of the plug-in learning stage itself.

## Score and Decision

**Originality:** The HPFL framework is novel—decoupling a shared backbone from per-client plug-ins and selecting at test time is a clean, well-motivated design. The SFL formulation is less original (the theorems are straightforward).  
**Importance of question:** The question is practically important: real FL clients do encounter out-of-distribution test data, and existing PFL methods fail at this task.  
**Support for claims:** The main claim (HPFL outperforms baselines on GFL-PM) is well-supported by Tables 2 and 3. The mechanism claim (accurate selection drives performance) is *not* well-supported—missing quantitative selection metrics. The privacy claim is unsupported.  
**Soundness of experiments:** The core experiments are sound in design (4 datasets, 3 architectures, standard heterogeneity splits) but incomplete in analysis (no selection accuracy metric, no k-NN ablation, no privacy evaluation).  
**Clarity of writing:** The paper is generally readable but the notation disconnect between theory and practice (Section 3.4 vs. Section 4.3) is confusing.  
**Value to community:** The HPFL framework is likely to be useful to FL practitioners; the idea is simple, effective, and extensible. The paper would be stronger with the evaluation gaps addressed.

The paper has a genuine practical contribution and strong empirical results for its core claim. However, the evaluation has a significant gap: the central mechanism (plug-in selection) is not quantitatively validated, and a secondary but strong claim (privacy) is unsupported. These are addressable in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
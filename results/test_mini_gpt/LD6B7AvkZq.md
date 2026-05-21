## Summary
The paper proposes a framework for studying language-model training on PCFGs through “subgrammars,” distinguishing inner and outer subgrammars and claiming recursive KL/loss decompositions over this structure. It then uses small-transformer experiments to visualize subgrammar loss curves, study subgrammar pretraining and representation similarity, and test length-vs-recursion-depth generalization on a nested-parentheses grammar. The topic is original and potentially valuable, but the central formal contribution is not soundly specified as written, and several empirical conclusions are overstated relative to the evidence.

## Strengths
- **Interesting and concrete problem setting.** The paper focuses on controllable PCFG-generated languages, where the true distribution is known and KL to the target grammar can in principle be measured directly. This is well aligned with the paper’s goal of studying learning dynamics rather than only final performance.
- **Useful distinction between two notions of subgrammar.** Definitions 3.3 and 3.5 distinguish “inner” subgrammars, intended to correspond to derivational subtrees, from “outer” subgrammars, intended to correspond to rule-restricted simpler grammars. Even though the definitions need substantial repair, this distinction is conceptually useful.
- **The recursion-depth experiment is a strong empirical idea.** Section 6 compares contexts of the form \((a)^i\) with contexts of the form \((^i\), where the next-token distribution is stated to be identical, and Figure 3 shows a clear contrast: final average prediction error 0.017 for long shallow contexts versus 0.173 at depth 200 for deep recursive contexts.
- **The paper includes preliminary representation evidence rather than only loss curves.** Section 5.2 reports CKA over 30 random seeds, and Table 1 shows attention-layer CKA increases after subgrammar pretraining, e.g. for two-layer transformers on full-grammar sequences from 0.249 to 0.303 after 20 epochs of pretraining.

## Weaknesses

### Fatal
None.

### Major
- **The central KL/subgrammar formalism is not well-defined enough to support the stated theorems.** Definition 4.2 defines the restricted divergence as  
  \[
  D_{\mathrm{KL}}(P_G\parallel Q)_A =
  \sum_{s\in\Sigma^*} P(s\mid\epsilon)P_G(A\mid s)
  \sum_{a\in\Sigma^*}D_{\mathrm{KL}}(P_G\parallel Q\mid \neg s),
  \]
  but the paper does not define the probability space for events such as “subgrammar \(A\) occurs after string \(s\),” nor how these latent derivational events are handled for terminal-string distributions. This matters because in a PCFG, subgrammar occurrences are derivation-level events, while the LM distribution is over terminal strings. Ambiguity, multiple occurrences of the same nonterminal, and different derivations for the same string all affect whether these restricted KL terms are identifiable or even well-defined.
- **The definition of inner subgrammar is ambiguous and may not produce a valid closed grammar.** Definition 3.3 says \(\mathcal{P}'\) is “the set of all rules with non-terminals in \(\mathcal{N}'\).” If this means rules whose left-hand side is in \(\mathcal{N}'\), their right-hand sides may contain nonterminals outside \(\mathcal{N}'\). If it means all nonterminals appearing anywhere in the rule must lie in \(\mathcal{N}'\), then rules are deleted and rule probabilities require renormalization in a way that can change derivability. This ambiguity directly affects Theorem 4.1’s claimed unique decomposition into a DAG of inner subgrammars and the later KL decompositions.
- **Theorem 4.1 overstates uniqueness without a precise construction.** The paper claims that every PCFG “can be uniquely decomposed into a hierarchy of its inner subgrammars” represented as a DAG with nodes labeled by nonterminal sets. As written, neither “hierarchy” nor “top-level subgrammar” is defined in the main formalism. A unique graph-theoretic decomposition might be possible if the authors mean something like strongly connected components of the nonterminal dependency graph, but that is not the same as uniqueness over arbitrary subgrammars under Definition 3.3. The theorem needs explicit assumptions and an exact construction.
- **There are algebraic/sign errors in the formal preliminaries and motivating KL derivation.** Definition 3.7 defines \(\mathcal{L}(\theta)=\mathbb{E}_{s\sim P}[-\log Q_\theta(s)]\) but then writes \(\hat\theta=\arg\max_\theta \mathcal{L}(\theta)\), even though this loss should be minimized. Definition 3.8 defines Shannon entropy as \(\mathbb{E}[\log P(s)]\), the negative of the usual entropy, while Proposition 3.9 uses the standard relation \(\mathcal{L}=D_{\mathrm{KL}}+H(P)\). In Section 4.2, Eq. (4) appears to turn sums of log-probability differences into ratios of logs, e.g. \(\log P/\log Q\), which is not the KL algebra. These errors are especially damaging because the paper’s main contribution is a theorem suite about KL/loss decompositions.
- **The learning-dynamics claims are stronger than what the decomposition and figures establish.** Figure 1 is described as showing “how, throughout all stages of learning, the KL divergence is the sum over the corresponding loss for each subgrammar.” But if the decomposition is exact by construction, plotting the sum is primarily an accounting identity, not evidence that transformers learn subgrammars independently or in a meaningful “parallel” sense. Figures 1 and 2 show several losses decreasing over training, but the paper gives no operational definition of parallel learning, no threshold or statistical criterion, and no control distinguishing parallel acquisition from shared exposure or frequency effects. Corollary 4.7 is also explicitly “stated informally” and assumes a non-interference condition that is close to the desired conclusion.
- **The representation and curriculum claims are overinterpreted.** Section 5.2 claims pretraining “definitively” yields representations aligned with grammar substructure. However, Table 1 mainly shows increased cross-seed attention-layer CKA, while MLP CKA is mixed or decreases in some settings, e.g. two-layer full-grammar MLP CKA drops from 0.535 to 0.511 after 20 epochs. Higher cross-seed CKA after a shared curriculum can reflect reduced optimization variance or easier early distributional statistics, not necessarily grammar-structural alignment. The cosine-similarity analysis in Section 5.2 is closer to the claim, but the paper does not state controls for length, frequency, derivational probability, or token-position confounds, and it uses the “top quantile of seeds,” which can inflate apparent effects if selection and analysis are not clearly separated.

### Minor
- **The large-language-model claim is not supported by systematic evidence.** The abstract says the recursion-depth limitation applies “even [to] large language models,” but the main text provides only an anecdotal GPT-5.1 Instant arithmetic test with 5 shallow and 5 deep examples, while footnote 3 correctly says these tests “should not be interpreted as direct evidence.” The controlled small-transformer result is interesting on its own; the broader frontier-model claim should be removed or backed by a systematic evaluation.
- **The recursion-depth experiment should be framed more carefully as out-of-distribution extrapolation.** Section 6 tests very deep but grammatically valid contexts up to depth 200. If these contexts have very low probability under the PCFG training distribution, failure on them is evidence about extrapolation to rare/deep contexts, not necessarily about whether the model “knows syntax” in-distribution.
- **The main text does not give enough experimental detail to evaluate the strongest empirical claims.** For several figures, the core grammar definitions, training setup, KL estimation procedure, and evaluation details are deferred or only briefly described. This is not fatal if the appendix contains them, but the paper’s main claims rely heavily enough on these choices that the essentials should be visible in the main text.
- **The claims about child-language acquisition are underdeveloped.** The paper says transformers learn subgrammars in parallel “unlike children,” but it does not formalize a developmental-stage analogue in the PCFG setting. This should be softened unless the paper defines and tests a precise notion of staged acquisition.

### Trivial
None.

## Nice-to-Haves
- Add a systematic baseline for subgrammar pretraining: compare true-subgrammar pretraining against length-matched, frequency-matched, probability-matched, and random full-grammar subsets.
- Report uncertainty for CKA and loss results across seeds, especially because some Table 1 differences are modest.
- Quantify “parallel learning” using a pre-specified criterion such as synchronized reduction in normalized excess loss, simultaneous threshold crossing, or measured gradient interference between subgrammar-restricted losses.
- Present a minimal worked PCFG example where the subgrammar DAG, restricted KL terms, and counting of multiple subgrammar occurrences are all explicitly computed.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Removed: generic claims that the paper addresses an important problem.** The topic is interesting, but this is not a substantive strength unless tied to specific contributions.
- **Removed: treating Theorem 4.3 / Corollary 4.4 as an established “exact loss decomposition” strength.** The paper states such results, but the definitions of restricted KL and subgrammar occurrence are not sufficiently well-defined as written, so this cannot be retained as a verified strength.
- **Removed: treating Theorem 4.1 as a verified formalization strength.** The paper’s distinction between inner and outer subgrammar is useful, but the uniqueness theorem is not justified by the definitions provided in the main text.
- **Removed: claims about missing related work.** These cannot be verified from the paper alone and should not drive the assessment.
- **Removed: formatting or parser-artifact concerns.** Any issues that could be due to PDF extraction, typography, line breaks, or missing symbols are not counted.
- **Removed: criticism that would rely only on the absence of appendix material.** The appendix is stripped from the provided text, so I do not fault the paper for omitted appendix proofs or details. The retained criticisms concern definitions, theorem statements, equations, and claims visible in the main paper.

## Novel Insights
The paper’s most promising insight is that PCFG learning dynamics can be studied not just at the whole-language level but by assigning loss contributions to derivational substructures. If made rigorous on a derivation-level probability space, this could provide a useful lens for connecting grammar structure, optimization, and curriculum effects. However, in its current form the paper conflates three different ideas—an autoregressive loss accounting identity, a derivation-level subgrammar decomposition, and a learning-dynamics claim about parallel acquisition—and the main contribution would be much stronger if these were separated.

## Suggestions
- Rebuild Section 4 on an explicit probability space: state whether \(P_G\) is a distribution over terminal strings, derivations, or string–parse pairs; define subgrammar occurrence events; specify how ambiguous grammars and multiple occurrences are handled.
- Define inner subgrammars with a closure condition on RHS nonterminals, or explicitly define the graph-theoretic quotient/decomposition being used.
- Correct the loss/entropy signs in Definitions 3.7–3.8 and the algebra in Eq. (4).
- Rephrase the theory as a decomposition of expected autoregressive token loss over derivation-labeled spans unless the authors can prove the decomposition directly for terminal-string distributions.
- Separate “loss decomposes over substructures” from “models learn substructures in parallel.” The latter needs a measurable definition and experiments designed to distinguish parallel acquisition from shared training dynamics.
- For representation alignment, match sequence groups by length, token frequency, derivational probability, and diagnostic token position; avoid post-hoc seed selection or clearly separate seed selection from the final analysis.
- Remove or substantially qualify the claim about large language models unless a systematic large-model evaluation is added.

## Overall Evaluation
- **Originality:** The subgrammar-centered framing for PCFG language modeling is original and potentially fruitful.
- **Importance:** Understanding learning dynamics on controlled formal languages is a worthwhile research question, especially for probing compositional and recursive structure.
- **Support for claims:** The central claims are not well supported. The formal claims rely on underdefined objects, and the empirical claims about parallel learning and representation alignment exceed the evidence.
- **Soundness of experiments:** The nested-parentheses depth experiment is a good controlled experiment. The curriculum and representation analyses are suggestive but need stronger controls and uncertainty reporting.
- **Clarity:** The paper is readable at a high level, but the formal sections contain serious definition and notation problems.
- **Value to the community:** The topic and experimental ideas could be valuable after substantial revision, but the current submission is not yet reliable enough as a theoretical contribution.

## Score and Decision

### Calibration and Anchors

**Round-1 bracket.** The initial calibration placed this paper between the weak formal-language/theory anchors around 3–4 and the stronger formal-language empirical/theory anchors around 5–7. Because the paper has more concrete empirical content than the weakest anchors but its central theorem suite is substantially underdefined, the round-1 bracket was **3.5 to 4.5**.

**Round-2 narrowing.** Round 2 retrieved several closer anchors in the 3.5–5 range. Compared with the 5.0 anchor on hierarchical filtering, this paper is weaker because the central theoretical object is less well-defined and the evidence for the learning-dynamics claim is less convincing. Compared with the 3.5–3.75 anchors on overclaimed training-dynamics/theory papers, this paper has somewhat more concrete controlled experiments, especially Figure 3, but similarly overclaims from an underdeveloped formalism. This places it near **4.0**, below borderline acceptance.

### Retrieved anchors and comparison

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uOnElfFuey.md`, avg 3.00, Round 1 — Similar formal-language interpretability setting, but this paper has broader and more interesting empirical scope; current paper is somewhat stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NSBP7HzA5Z.md`, avg 3.00, Rounds 1 and 2 — An overclaimed transformer-concept paper with weak grounding; current paper is stronger due to concrete PCFG experiments, but still overclaims.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OW5Gf4cse1.md`, avg 3.00, Round 1 — A synthetic small-LM dynamics paper with limited support; current paper is somewhat stronger in originality but has serious formal flaws.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4y3GDTFv70.md`, avg 3.25, Round 1 — A broad theoretical LLM paper with weak support; current paper is more concrete but still formally unreliable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0pLCDJVVRD.md`, avg 7.00, Round 1 — A much stronger formal-language/emergence paper with clearer empirical support; current paper is substantially weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1lFZusYFHq.md`, avg 6.20, Round 1 — Stronger transformer-theory paper with more developed analysis; current paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fp77Ln5Hcc.md`, avg 4.50, Rounds 1 and 2 — Very close topical anchor on nested structures; current paper has a nice depth experiment but a less sound central theory, so slightly weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hNkXTqDrfb.md`, avg 3.75, Rounds 1 and 2 — Similar in that it makes broad learning-dynamics claims from a simplified formal setup; current paper is comparable, perhaps slightly stronger empirically but similarly overclaimed.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/STUGfUz8ob.md`, avg 7.60, Round 1 — Much stronger theoretical/empirical transformer reasoning paper; current paper is far weaker in formal soundness.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/n2NidsYDop.md`, avg 8.67, Round 1 — A substantially stronger theory paper with sharper claims and proofs; current paper is not comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Tzh6xAJSll.md`, avg 7.60, Round 1 — Stronger theory/experiment paper with clearer validation; current paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/d8w0pmvXbZ.md`, avg 8.00, Round 1 — Strong systems/empirical anchor with robust evidence; current paper is much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sprjE7BTZR.md`, avg 3.75, Round 2 — Similar in having ambitious formal claims with underdefined machinery; current paper is comparable but somewhat more empirically interesting.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MRPCIForrE.md`, avg 4.75, Round 2 — A theoretical reasoning paper with concerns but less central definitional breakdown; current paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eRkNNQRppH.md`, avg 3.50, Round 2 — Similar overclaiming from training curves; current paper is slightly stronger because of its PCFG framing and recursion experiment.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/F0Zd3knG9j.md`, avg 5.00, Round 2 — A PCFG/structured-data transformer paper with alternative-interpretation concerns; current paper is weaker because its central formal definitions are less sound.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aWLQTbfFgV.md`, avg 6.25, Round 2 — Stronger formal-language neural-network paper with clearer task/evaluation alignment; current paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/b5lXUwZiD3.md`, avg 5.25, Round 2 — Empirical transformer-on-sequence-model paper with clearer experimental basis; current paper is weaker formally.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/v675Iyu0ta.md`, avg 5.60, Round 2 — Stronger interpretability/OOD empirical paper; current paper is weaker in evidence and formal grounding.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hFQZmKFtlT.md`, avg 3.50, Round 2 — Similar formal-grammar LM setting with weak support; current paper is slightly stronger but still in the reject range.

**Final score:** 4.0  
**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>  
MY FINAL DECISION: <decision>Reject</decision>
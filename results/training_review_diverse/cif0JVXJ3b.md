Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes a finer-grained typology of Knowledge Neurons (KNs), distinguishing Concept Neurons (sensitive to a single concept/entity) from Relation Neurons (sensitive to a relation across multiple instantiations). The authors apply this typology across multiple PLMs, analyze the distribution of KN types, and conduct boosting experiments for causal validation. They then extend the analysis to multilingual settings, constructing and releasing Multi-ParaRel (a multilingual version of ParaRel spanning 10 languages) and showing that KNs overlap across languages at rates far exceeding chance — and even extend to machine-generated (AutoPrompt) prompts. The core contributions are: (i) demonstrating that KNs come in different flavors (concept-like, relation-like, and intermediate) rather than being monosemantic, and (ii) uncovering substantial cross-lingual KN overlap suggestive of a partially shared, language-agnostic knowledge retrieval mechanism.

## Strengths

- **Distributional evidence for distinct KN flavors is clear and well-presented.** Figure 2a shows that many KNs appear in only one instantiation (concept-like), while a continuous range appears across multiple instantiations. This distributional finding directly supports the claim that KNs are not uniformly monosemantic and that a simple concept-vs-relation typology captures real variation — even before the causal experiments. The paper's own framing (Section 5.2) is appropriately measured, noting that it "challenges the simplistic interpretation of assigning neurons exclusively to concepts."

- **Cross-lingual KN overlap is demonstrated with strong quantitative evidence.** The numbers are compelling: for Llama-2-7b, 189 shared KNs between language pairs vs. only 2 expected by random chance; for mBERT, 710 shared vs. ~100 expected (Section 6.2). The decay pattern across the number of languages (~(number of languages)^(-2.04)) is qualitatively different from a random-sharing baseline, providing robust evidence that the overlap is not an artifact of pairwise coincidence. This extends prior work (Chen et al., 2024) from one language pair to 10 languages, and the analysis of decay across languages is a methodological improvement.

- **Multi-ParaRel dataset is a concrete, reusable resource.** The dataset covers 10 languages with ~17 prompts per relation per language (after filtering ~10), is compatible with autoregressive models, and comes with a translation/curation pipeline for extension. This enables reproducible multilingual KN research and is a practical contribution independent of the paper's analytical claims.

- **The AutoPrompt extension.** Despite an acknowledged potential confound (both AutoPrompt and KNs use gradient-based signals), the finding that KNs overlap substantially (≥80%) between natural and machine-generated prompts is an interesting stress-test of the language-agnostic hypothesis and provokes useful discussion.

## Weaknesses

### Fatal
None.

### Major

- **Causal validation of the typology is mixed and incomplete.** The boosting experiments (Section 5.3) test three predicted effects: (i) boosting concept neurons increases P@1, (ii) relation neurons have weaker effects on P@k than concept neurons, and (iii) relation neurons affect CCP@k more than concept neurons. Effect (i) holds for all 6 models — this is the strongest result. However, effect (ii) holds for only 2/6 models, and effect (iii) holds for 4/6. Only 2 models (bert-large-uncased, gemma-2-9b) exhibit all three effects, and even then only under restrictive thresholds (t_r=0.9). The paper candidly describes these as "mixed results" and suggests noise or attribution-method limitations as possible explanations — but these explanations are speculative and do not remedy the gap. The paper's *distributional* evidence for the typology is robust, but the causal evidence that concept and relation neurons are *functionally distinct* in the way predicted is only partially supported. This weakens the paper's stronger claim about distinct functional roles.

- **Cross-lingual KN overlap is well-established, but the interpretation as a "shared, language-agnostic knowledge base" (Conclusion, Section 8) overreaches the evidence.** Section 7 correctly notes that "parallel activation does not equate to shared functionality" but the paper does not test whether shared KNs mediate the *same factual predictions* across languages. The overlap could reflect correlated gradient sensitivity in a multilingual embedding space rather than a shared knowledge-retrieval mechanism. The paper partially controls for this by computing overlaps at the relation level (same relation across languages), but this still falls short of demonstrating that the same neurons support the same <h,r,t> facts in different languages. The headline claim therefore exceeds what the evidence supports — the overlap finding is a strong *correlational* signal but not a causal demonstration of shared knowledge representation.

### Minor

- **The AutoPrompt overlap finding has an acknowledged but unaddressed confound.** The paper notes (Section 6.3) that "both Autoprompt and KNs are gradient based" as a possible confound for the ≥80% overlap, but provides no control experiment (e.g., using a non-gradient-based knowledge localization method, or comparing against a baseline of random prompts matched for token distribution). The confound is honestly disclosed but leaves an important alternative explanation on the table.

- **The typology does not test for cross-relation polysemy.** A neuron classified as a "relation neuron" for the "capital of" relation (appearing in ≥90% of its instantiations) could also be sensitive to other relations involving the same entities (e.g., "located in"). The classification is within-relation by construction, so a neuron could appear relational for one relation while also encoding entity-level information from another. The paper acknowledges intermediate categories but does not examine this cross-relation dimension.

- **Model-specific patterns in the boosting experiments are unexplained.** The paper notes that only 2/6 models show all three effects but does not analyze why (e.g., does failure correlate with model size, layer distribution of KNs, task accuracy?). The "noise" attribution is a placeholder rather than an analysis.

### Trivial
None worth listing individually.

## Nice-to-Haves

- **Cross-lingual causal evidence would substantially strengthen the shared-knowledge claim.** The most impactful follow-up would be to test whether shared KNs causally mediate the same factual predictions across languages — e.g., by editing or boosting shared KNs in one language and measuring effects on predictions in another language. This would distinguish shared functional roles from correlated activation patterns.
- **Per-neuron probing across individual prompts** could reveal whether a shared KN responds to the same entity pairs (e.g., France/Paris) in both languages, or to different instantiations of the same relation. This would add specificity to the overlap finding.
- **A non-gradient-based control for the AutoPrompt experiment** (e.g., using a different knowledge localization method, or comparing against synthetic prompts matched for distributional properties) would help isolate whether the overlap reflects shared knowledge mechanisms or a gradient-attribution artifact.

## Removed Points

The following points from the reviewer inputs were removed with justification:

- *Criticism that "only 2/6 models show all three predicted behaviors" treated as fatal flaw* — Partially removed from its fatal framing and downgraded to Major. The paper's main evidence for the typology is the distributional analysis (Figure 2a), which is independent of the boosting experiments. The paper is honest about the mixed results. Effect (i) holds for all 6 models, and the paper does not claim perfect categorization. The critic overstates the centrality of the causal experiments relative to the paper's actual claims.
- *Demand for per-neuron probing and cross-lingual editing experiments presented as missing essentials* — Moved to Nice-to-Haves. These are significant additional studies that go beyond the paper's stated scope. The paper provides relation-level analysis, which is a reasonable starting point.
- *Suggestion to use ROME as a non-gradient-based control for AutoPrompt* — Moved to Nice-to-Haves. ROME is a knowledge *editing* method, not a neuron attribution method; adapting it for cross-model KN comparison is not straightforward and would require significant methodological development.
- *Criticism that "the paper does not include a systematic analysis of what the shared KNs across languages actually encode"* — Moved to Nice-to-Haves. The paper provides analysis at the relation level (same relation shared across languages), which is a meaningful intermediate granularity between nothing and per-prompt probing.

## Novel Insights

The reviews raise a genuinely interesting tension: the paper's two main contributions pull in opposite evidentiary directions. The typology claim benefits from being descriptive — the distribution analysis cleanly shows different KN flavors without needing causal confirmation. But the cross-lingual claim suffers from being *only* descriptive — the overlap is strong statistically but ambiguous functionally, and the paper's own Section 7 concedes that parallel activation does not guarantee shared function. The net effect is that the paper convincingly shows KNs are *not* simply monosemantic and that they *are* systematically shared across languages, but the functional interpretation of both findings remains less certain than the paper's strongest language suggests. This suggests the paper would be strengthened by reframing its conclusions as more explicitly raising the question of functional sharing rather than answering it.

## Suggestions

1. **Reframe the cross-lingual conclusions** to match the correlational nature of the evidence. Phrases like "shared language-agnostic knowledge base" (Conclusion) imply functional sharing that the evidence does not directly establish. "Systematic cross-lingual overlap suggesting a shared retrieval substrate" would be more precise.

2. **Separate the typology's evidentiary pillars more clearly.** The distribution analysis (Figure 2a) is the primary evidence for "different flavors"; the boosting experiments are a secondary causal check. A brief methodological note clarifying that the typology is defined by the distribution and *tested* causally via boosting would prevent readers (and reviewers) from conflating these.

3. **Add a simple control for the AutoPrompt confound** — even comparing the observed overlap against overlap with randomly sampled tokens or synthetic prompts with similar token distribution would help assess whether the gradient-based confound is the primary driver of the high overlap.

4. **Include a brief analysis of why the boosting experiments fail for certain models.** A simple correlation analysis (e.g., does failure correlate with model size, KN layer distribution, or task accuracy P@1?) would turn the unexplained "noise" into a predictive observation, potentially refining the typology.

## Score and Decision

The paper makes genuine contributions: the distributional analysis revealing KN variation, the quantitatively rigorous demonstration of cross-lingual KN overlap across 10 languages (with far-above-chance statistics), and the release of the Multi-ParaRel dataset. However, the causal validation of the proposed typology is only partially successful (one of three predicted effects holds universally; the others are model-dependent), and the interpretation of cross-lingual overlap as a "shared knowledge base" exceeds what the correlational evidence supports. These are real limitations but not fatal — the paper is transparent about them and the core descriptive findings remain novel and useful. A revision could strengthen the framing and add selective additional analyses.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
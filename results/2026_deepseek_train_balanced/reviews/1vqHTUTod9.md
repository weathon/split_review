## Summary

This paper introduces **PrivQA**, a multimodal benchmark (4,678 textual + 2,000 visual QA examples) for evaluating whether language models can follow access-control instructions to withhold information about protected populations (citizenship, age, occupation, public position) and protected information categories (location, profession, education, etc.). The authors propose **Self-Moderation** — an iterative generate-moderate-authorize prompting pipeline — and evaluate GPT-3.5, GPT-4, LLaMA-2, and IDEFICS. Key findings: Self-Moderation improves protection scores over naive instruct prompting, but models exhibit popularity bias (less protection for less-known individuals), rely on visual shortcuts for citizenship determination, and are catastrophically vulnerable to simple jailbreaking and multi-hop attacks.

---

## Strengths

1. **First purpose-built benchmark for access-control instruction following for information protection.** PrivQA repurposes five existing QA datasets with clear category definitions motivated by GDPR, covering both textual and visual modalities. Prior work focused on differential privacy, unlearning, or model editing; this is the first standardized evaluation of instruction-based selective withholding.

2. **Entity-popularity bias is rigorously documented and quantified.** By stratifying protection sensitivity by Wikipedia pageview-based popularity (Figure 5), the paper shows sensitivity drops from ~80% to ~20% (GPT-3.5) and ~100% to ~60% (GPT-4) from head to tail entities. This identifies a concrete, measurable failure mode where less well-known (more private) individuals receive *less* protection — a non-obvious finding that goes beyond high-level bias hand-waving.

3. **Systematic red-teaming across three attack vectors with measured success rates.** The paper reports Attack Success Rates (ASR) for: adversarial prefix prompts (e.g., BetterDAN raises ASR from 3.0% to 26.5% for GPT-3.5 on President category), visual prompt injection (rendering misleading text raises ASR from ~27–30% to ~84–95% for IDEFICS-9B), and multi-hop questions (100% ASR on some protected information categories like location). These are quantified, not anecdotal.

4. **Empirical validation that instruction-based approaches outperform weight-editing at group level.** The ROME comparison (Figure 6) shows protection score collapsing to 0% and near-zero F₁ on both protected and control groups within 100 edits, while Self-Moderation remains at ~70%. This validates the paper's Related Work claim (line 67) that model editing cannot generalize to complex information categories, and provides a concrete reason to prefer instruction-based approaches.

5. **Visual shortcut failure mode identified.** The paper surfaces that IDEFICS uses physical appearance as a "shortcut" for citizenship (lines 222–224), which would disproportionately misclassify minorities within a protected population — a specific, testable failure pattern grounded in prior work on demographic bias.

---

## Weaknesses

### Major

- **Framing gap between "privacy protection" and what the benchmark actually measures.** The title, abstract, and conclusion frame PrivQA as a privacy protection benchmark. What it measures is whether models can follow categorical withholding instructions for *public Wikipedia knowledge about public figures*. Real privacy risks involve memorized, non-public data (phone numbers, medical records, financial information) that individuals never consented to being disclosed. The benchmark tests an important *proxy* capability — instruction-following for selective response in a "simulated scenario" (line 7) — but the proxy-to-target gap is substantial and largely unaddressed. The paper acknowledges using public figures in one sentence (line 86: "This makes the evaluation slightly less realistic") but never discusses whether findings about popularity bias, jailbreak vulnerability, or self-moderation improvements would transfer to genuine privacy scenarios. This overclaim runs through the paper's core framing and needs to be corrected for the contribution to be accurately assessed.

### Minor

- **Self-Moderation lacks comparison to alternative prompting strategies.** The technique (generate → moderate → iteratively authorize with "Are you sure?") is listed as contribution #2 but is compared only against simple "Instruct Prompting." It is not compared against other established prompting-based safety approaches (e.g., chain-of-thought with privacy instructions, self-ask, constitutional AI prompting with a privacy constitution). Without this, it is unclear whether the gains come from the specific design of Self-Moderation or from any multi-step verification prompting approach.

- **Multi-hop attack construction is underdescribed for reproducibility.** The paper states that "2-hop question templates" were crafted "customized to different information-types" (line 334–336) but gives no examples of the templates, no count of how many were constructed per category, and no detail on whether they are hand-crafted or templated. Given that the 100% ASR finding on location information is one of the paper's most striking results, this limits reproducibility.

- **No validation of "none" as the abstention signal.** Models are instructed to output "none" to indicate abstention (line 175). While the two-metric evaluation (Protection Score + Response F₁) partially addresses concerns about whether models are genuinely refusing versus guessing "none" for hard questions, a small-scale human validation study on a sample of outputs would strengthen confidence in the metric.

### Trivial

None.

---

## Nice-to-Haves

- Per-category breakdowns for visual tasks (the paper reports average ~65% protection for IDEFICS but doesn't break down by visual category, which would be informative given the visual shortcut finding).
- Deeper analysis of why LLaMA self-authorization degrades performance (the paper mentions it "often overturns previous decisions" but doesn't quantify frequency or analyze mechanism).
- Discussion of the computational cost of iterative Self-Moderation (multiplies inference cost by steps + 1).
- Variance or prompt-sensitivity reporting across multiple prompt templates.

---

## Removed Points

These points were flagged for removal during filtering and should be treated with caution:

- **Harsh Critic: "ROME comparison is uninformative and should be removed."** — REMOVED. The comparison is informative. The paper explicitly states in Related Work (line 67) that model editing "cannot generalize to the more complex notions of information categories" and the experiment validates this claim. It also provides a concrete demonstration of why instruction-based approaches are preferable for group-level protection, directly supporting the paper's motivation. This is not a weakness but a legitimate strength.

- **Harsh Critic: "Self-moderation is a straightforward prompting chain" presented as a critique of contribution quality.** — Demoted from potential fatal/major to Minor (lack of comparison to alternatives). The paper is primarily a benchmark paper, not a methods paper, and straightforwardness of a technique used for evaluation is not a weakness per se.

---

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the framing gap as the primary issue but do not produce a novel observation about the paper's content that the paper itself does not articulate.

---

## Suggestions

1. **Reframe the benchmark's claims** to match what it actually measures: "selective information withholding" or "categorical instruction compliance" rather than "privacy protection." The title "Can Language Models be Instructed to Protect Personal Information?" should be adjusted. Add a limitations paragraph discussing what additional validation would be needed to connect these results to real privacy scenarios involving genuinely sensitive, non-public data.

2. **Add multi-hop attack construction details** — provide at least one example template per category and state the number constructed — to improve reproducibility.

3. **Run a small human validation study** (e.g., 100–200 examples) to verify that "none" outputs correspond to genuine abstention rather than an output heuristic for difficult questions.

4. **Compare Self-Moderation against at least one alternative prompting strategy** (e.g., constitutional AI prompting with a privacy-focused constitution, or chain-of-thought with privacy instructions) to establish what the specific pipeline design adds over a reasonable alternative.

---

## Score and Decision

The benchmark is well-constructed, fills a genuine gap, and produces solid, practically important empirical findings (popularity bias, visual shortcuts, catastrophic jailbreak vulnerability). The primary weakness is a framing overclaim in the title and throughout — the benchmark measures instruction compliance for categorical withholding of public knowledge, not privacy protection in a meaningful sense. This is fixable through honest rebranding and does not invalidate the core contribution. With revisions to the framing, this would be a solid addition to the LLM safety evaluation literature.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have enough information to write the final review. Let me consolidate my assessment of the paper and the reviewers' claims.

## Summary

This position paper argues that racial categories should be abandoned in ML research whenever possible, as they reinforce essentialist views, fail to account for identity complexity (particularly for mixed-race individuals), and are dominated by U.S.-centric taxonomies with limited global applicability. The paper supports this position through: (1) a critique of U.S.-centrism in ML fairness research (with an empirical analysis of 78 ICML/CVPR papers), (2) a systematic analysis showing that all five possible approaches to handling mixed-race identity within categorical race taxonomies are fundamentally inadequate (Section 4), (3) evidence of racial reification and stereotyping in generative AI (Section 5), and (4) a proposed research agenda that replaces racial categories with constitutive features, grounded in constructivist accounts of race and connected to individual fairness and multi-calibration in ML (Section 6).

## Strengths

- **Systematic demonstration that categorical approaches to mixed-race identity are fundamentally unsatisfiable (Section 4)**: The five-approach enumeration (A–E) is a genuine analytical contribution. It shows that forcing mixed-race individuals into single categories (Approach A) denies identity, lumping them into a single "Mixed-race" bucket (Approach B) erases internal diversity, subsuming under "Other" (Approach C) exacerbates exclusion, exhaustive enumeration (Approach D) creates combinatorial explosion AND loses categorical relationships, and multi-labeling (Approach E) faces feasibility barriers. This analysis demonstrates the problem is structural to categorization itself, not fixable by better category design.

- **U.S.-centrism as an underappreciated structural critique (Section 3)**: The empirical analysis of 78 ICML/CVPR papers showing that racial classifications in ML overwhelmingly derive from U.S. census categories, contrasted with GDPR and European legal frameworks that actively reject racial classification, is both novel and consequential. It reveals a fundamental parochialism in how ML fairness research conceptualizes its central variable.

- **Interdisciplinary synthesis across social science, law, and ML**: The paper draws productively on anthropology (Kroeber, Smedley & Smedley), legal scholarship (Hu & Kohler-Hausmann on constitutive features), economics (Rose on race functions), and social psychology (Levin & Banaji on the FRL illusion), integrating these perspectives into a coherent argument about why categorical race is conceptually flawed—a synthesis that, to my knowledge, has not been done before for the ML fairness community.

- **Acknowledgement of the strongest counterargument**: Section 7's engagement with strategic essentialism—the worry that removing categories harms marginalized groups who rely on them for visibility—is honest and substantive. The paper concedes the legitimacy of strategic essentialism while distinguishing it from the uncritical, externally imposed categorization common in ML.

- **Novel experimental illustrations**: The replication of the Face Race Lightness Illusion in VQA models (Figure 3) is a novel finding that demonstrates entanglement between phenotypic features and brightness perception in AI systems, supporting the argument that fairness evaluation must go beyond race-level or even skin-tone-level analysis.

## Weaknesses

### Fatal
None.

### Major

- **The "constitutive features" proposal is not conceptually distinguished from "use more fine-grained racial features"**: The paper's central constructive proposal is to replace racial categories with "constitutive features"—skin tone, hair texture, name-based ethnicity, etc. But if constitutive features are the mechanisms through which racialization and discrimination operate (as the paper itself argues, drawing on Hu & Kohler-Hausmann), then using them in fairness auditing is essentially using race decomposed into its constituent parts. The paper needs to address whether this move is substantively different from "use more fine-grained racial features" or whether it is a semantic relabeling that preserves the same essentialist logic at a finer granularity. The paper gestures at this—distinguishing its approach from "proxies" for race by rejecting the assumption of a causal link to a latent racial variable (Section 6.1)—but this distinction is asserted more than argued, and is insufficient to resolve the tension. If a practitioner replaces "race=Black" with "skin tone=dark + hair texture=afro + name-based ethnicity=African," has anything been gained beyond precision? The paper owes the reader a clearer account of what is gained beyond granularity.

- **"Whenever possible" does heavy lifting but is never defined**: The qualifier "whenever possible" appears in the paper's central claim on line 37 and line 63 but is never operationalized. Section 7 concedes that "there can be situations where their use is warranted," but does not specify the boundary conditions. Is it "possible" when legal regimes require it? When communities demand it? When no viable alternative detection method exists? The failure to clarify what "whenever possible" actually means makes the position difficult to engage with productively—one can always agree with "do X whenever possible" if "possible" remains undefined. This is not just a precision complaint: it affects whether the paper's position is actionable and debatable.

### Minor

- **The Europe comparison is presented as supporting evidence but also illustrates a cautionary risk**: Section 3 presents Europe's institutional avoidance of racial categories as contextually relevant, and Section 6 honestly acknowledges the Braveman & Parker Dominguez warning that "abandoning the term 'race' has not been accompanied by routine monitoring of health and well-being according to markers of the ethnic groups that are relevant to racism." However, the paper does not fully grapple with whether this constitutes evidence against the position it puts forward—that is, whether removing race categories from ML could reproduce Europe's failure to detect discrimination at scale. The paper acknowledges the challenge and uses it to motivate alternatives, which is reasonable; a deeper analysis of this risk would strengthen the paper but its absence is not fatal.

- **Generative AI stereotyping experiment supports reification critique but not abandonment uniquely**: Section 5 shows that Stable Diffusion and Midjourney produce stereotypical outputs, which supports the claim that AI reinforces racial stereotypes. However, the problem demonstrated is stereotyping in generative models, not the use of race categories in fairness auditing per se. The connection to the central argument (abandon categories) is indirect and requires an inferential step the paper does not make explicit.

- **Approach D's combinatorial explosion argument is weakened by typical values**: The paper argues that Approach D (all mixed categories separately) leads to "combinatorial explosion" since k categories yield 2^k − 1 labels. For typical k values (5–8), this yields 31–255 possible labels, which is computationally manageable. The paper's second argument against Approach D (categorical nature means "Black/Hispanic" stands in the same relationship to "Black" as to "White") is the stronger one, but the combinatorial explosion claim is overstated for practical k.

- **The EDTAL principles (Section 6.3) are generic**: The four principles (Early engagement, Decision-making power, Transparency, Localized approaches) are sensible but could apply to virtually any participatory AI context. They do not specifically address how to operationalize fairness without racial categories, which is the distinct challenge this paper faces.

### Trivial
None.

## Nice-to-Haves

- A concrete worked example showing that constitutive-feature-based auditing can detect biases that race-category-based auditing misses (or at least achieves comparable detection) on an existing dataset—even a small-scale illustration would significantly strengthen the transition from "these alternatives exist conceptually" to "these alternatives can work."

- A clearer definition or set of principles for what "whenever possible" means in practice—e.g., "categories are warranted when (1) demanded by the affected community, (2) required by legal regime, or (3) no constitutive-feature-based alternative exists for the specific context."

- A more explicit argument for why constitutive features are substantively different from finer-grained racial proxies, beyond the current distinction that they reject a "causal link" to latent race.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The position is not truly held because Section 7 concedes exceptions"**: The harsh critic argues that the Section 7 concessions ("strategic essentialism is legitimate," "situations where their use is warranted") substantially narrow the claim, making the paper dishonest about its own position. However, the qualifier "whenever possible" was present from the abstract. Section 7 merely specifies what "whenever possible" entails. A position paper that says "do X whenever possible but acknowledge exceptions" is making a coherent, defensible normative claim—and acknowledging exceptions is a feature of intellectual honesty, not a contradiction. The real problem is that "whenever possible" is undefined (see Major weakness above), not that the paper doesn't truly hold its position.

- **"The proposed alternatives don't justify the strength of abandonment"**: The harsh critic demands that the paper demonstrate viable alternatives as a condition for advocacy. But this frames the position paper as requiring proof of feasibility rather than arguing for a direction. The paper explicitly presents its alternatives as research directions, not as completed solutions. For a position paper that argues "the field should move in this direction," acknowledging limitations of proposed paths is appropriate. The critique that alternatives are preliminary has some merit (reflected in the "constitutive features" weakness above), but the demand for operationalized alternatives exceeds what a position paper must deliver.

- **"Europe comparison undermines the position"**: The paper itself cites the Braveman & Parker Dominguez caveat and uses it as motivation for developing better alternatives. This is a reasonable editorial choice, not an unaddressed contradiction.

- **"The paper should be reframed around claim (A) rather than (B)"**: This is a strategic suggestion about framing, not a substantive weakness. The paper chooses to make a strong normative claim; that is its prerogative as a position paper. Telling the authors their paper would be "more honest" making a weaker claim is effectively demanding they hedge their position, which contradicts the purpose of position papers.

- **"The FRL illusion experiment's connection to the central argument is unclear"**: The paper uses it to support the argument that phenotypic features beyond skin tone matter for fairness evaluation—this is a support for using constitutive features rather than racial categories. The connection is present, just indirect (moved to Minor).

- **"Combinatorial explosion invalidates Approach D argument"**: The paper has two arguments against Approach D; the second (categorical relationship problem) is independent and stronger. The criticism of the first argument is valid but doesn't undermine the overall analysis of Approach D.

- **"Small sample sizes in experiments"**: Position papers may use illustrative experiments. The paper acknowledges small sample sizes (CFD-MR: 88 individuals; 30 images per prompt). For a position paper, these are adequate as supporting illustrations rather than primary evidence.

## Novel Insights

The most novel insight is that the mixed-race problem provides a structural—rather than contingent—argument against categorical race in ML. Prior critiques have argued that categories are U.S.-centric, poorly documented, or reductive. This paper shows that for a systematically growing segment of the population (mixed-race individuals now 10.2% of U.S. census respondents), all five logically possible ways of fitting them into categorical taxonomies fail. This is not a fixable implementation problem but a fundamental incompatibility between categorical representation and the structure of racial identity. A secondary insight is that the FRL illusion replicates in VQA models, suggesting that AI systems may internalize the same socio-cognitive biases that shape human racial perception—connecting social psychology findings directly to ML fairness evaluation design.

## Suggestions

- Provide 2–3 concrete boundary conditions for "whenever possible," framed as principles rather than exhaustive rules. For instance: "categories are warranted when the affected community explicitly advocates for their use; when legal compliance requires them; and when no feasible constitutive-feature-based alternative exists for the specific deployment context."

- Add 1–2 paragraphs explicitly addressing the "constitutive features = race by another name?" objection. Clarify whether the gain is purely granular precision, or whether there is a substantive conceptual shift (e.g., from treating race as a fixed attribute to treating discrimination as a context-dependent process involving multiple features).

## Score and Decision

**Calibration anchors:**

1. **PFRandBfSz** (avg 7.0, Accept/Oral): Argues AI innovation violating fundamental rights isn't real innovation. Strong position with rich argumentation, EU AI Act analysis, good engagement with counterarguments. This paper under review has similar interdisciplinary breadth and normative ambition but weaker alternative development and undefined boundary conditions. Below this anchor.

2. **USqNoPVhxx** (avg 7.33, Accept): Argues for broader conception of rigor in AI. Rich framework, well-argued with examples. This paper under review is comparable in conceptual ambition but has a clearer, more specific position and more empirical content; however, it has less operationalized alternatives. Slightly below this anchor.

3. **vFae5rRman** (avg 6.0, Accept): "Benchmarking is broken," PeerBench proposed. Strong critique with preliminary but more concrete alternative. This paper has better problem analysis (systematic mixed-race analysis, US-centrism critique) but less concrete alternatives. Comparable or slightly below.

4. **8ZH52QHIZV** (avg 5.33, Reject): XAI transparency paradigm wrong, DAN proposed. Alternative underdeveloped, lacks operationalization. This paper's problem analysis is significantly stronger (systematic, empirical, interdisciplinary), and its alternatives, while preliminary, are better grounded in existing ML literature (individual fairness, multi-calibration). Above this anchor.

5. **iOSHFKHQNP** (avg 5.67, Reject): Human-LLM alignment, preliminary alternatives. This paper has a more distinctive position, novel analytical contributions (mixed-race analysis), and better empirical grounding. Above this anchor.

6. **Omq9tUouSS** (avg 3.67, Reject): Symbol safety science, no alternative discussion. Far below this paper, which has genuine engagement with counterarguments and multiple illustrative experiments. Significantly above.

This paper's genuine contributions (the systematic mixed-race analysis, US-centrism critique, interdisciplinary synthesis, and novel VQA experiment) place it clearly above the rejected anchors. Its weaknesses (undefined "whenever possible," the constitutive-features conceptual gap, and preliminary alternatives) place it below the strongest accepted position papers. The mixed-race analysis alone is a substantial and novel contribution that justifies discussion. Overall, I place this paper between the vFae5rRman anchor (6.0) and the 8ZH52QHIZV anchor (5.33), slightly closer to 6.0 given the genuine analytical novelty.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
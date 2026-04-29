# Governments Should Mandate Tiered Anonymity on Social-Media Platforms to Counter Deepfakes and LLM-Driven Mass Misinformation

- Decision: Reject
- Scores: 8, 6, 6

## Abstract
This position paper argues that governments should mandate a three-tier anonymity framework on social-media platforms as a reactionary measure prompted by the ease-of-production of deepfakes and large-language-model-driven misinformation. The tiers are determined by a given user's $\textit{reach score}$: Tier 1 permits full pseudonymity for smaller accounts, preserving everyday privacy; Tier 2 requires private legal-identity linkage for accounts with some influence, reinstating real-world accountability at moderate reach; Tier 3 would require per-post, independent, ML-assisted fact-checking, review for accounts that would traditionally be classed as sources-of-mass-information.

An analysis of Reddit shows volunteer moderators converging on comparable gates -- karma thresholds, approval queues, and identity proofs -- as audience size increases, demonstrating operational feasibility and social legitimacy. Acknowledging that existing engagement incentives deter voluntary adoption, we outline a regulatory pathway that adapts existing US jurisprudence and recent EU-UK safety statutes to embed reach-proportional identity checks into existing platform tooling, thereby curbing large-scale misinformation while preserving everyday privacy.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This position paper argues that governments should mandate a tiered anonymity framework on social media platforms to counter the growing harms of deepfakes and LLM-driven misinformation. The authors propose a three-tier system where identity and verification obligations grow proportional to the user's reach and influence. Here tier 1 preserves pseudonymity for small accounts, tier 2 introduces private identity verification and tier 3 imposes fact-checking before publishing and traceability. The paper uses Reddit moderation practices as empirical evidence, outlines a technical implementation pathway and looks at the regulatory frameworks in the EU and US. The position is that influence should be proportional to accountability and that the proposed tiered anonymity provides a framework to ensure privacy and responsibility in social media discussions.

### Strengths
The paper offers a well-written, legally informed proposal for regulating online anonymity in the age of LLMs and deepfakes. It supports the proposed model with empirical case studies e.g. Reddit, feasibility analysis and a detailed regulatory mapping across geographies. The discussion around different regulations is well-structured and shows that the proposal is legally grounded and not hypothetical. The Reddit case study adds credibility how tiered moderation could emerge organically. The paper covers both societal impact and practical feasibility of the proposed framework.

### Weaknesses
- The paper mentions "deepfakes" prominently in the title and abstract but appears not to touch upon this specific threat throughout the paper. This undermines the idea of the proposed framework.
- There are multiple nuanced identity concepts used e.g. conditional pseudonymity, proportional friction, identity calibration but lacks a clear taxonomy overview. This may or may not be obvious to the reader. A table contrasting anonymity models and obligations by country or policy context would help improve reader clarity.
- While Reddit provides a useful analogue, the applicability of community-driven governance to global-scale commercial platforms e.g. Meta, X is debatable and may be overstated. In lines 328-330, the claim that such moderation hierarchies are difficult to replicate is asserted without clear justification and source. 
- While the legal mapping is thorough, the paper does not directly address the practical and legal challenges of implementing such a framework in the US i.e. on how it would interact with the constitutional protections and potential resistance from commercially motivated platforms, which may pose practical constraints on the adoption.

### Questions
- Could the tier system unintentionally deter mid-tier creators from growing their audience due to additional burden or scrutiny?
- The authors assert that Reddit-style governance is difficult to replicate on commercial platforms but do not explain in detail why. What makes Reddit exceptional in this regard? Is it cultural, structural, legal or commercial?
- Have the authors considered how react thresholds may be gamed e.g. using bots or similar?
- Would it be helpful to include a summary table comparing anonymity obligations and legal constraints across different jurisdictions? This may strengthen the position of the paper.

### Presentation
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This position paper argues governments should mandate a three-tier anonymity framework on social media platforms to counter AI-generated misinformation and deepfakes. The framework scales identity obligations with user reach: Tier 1 preserves full pseudonymity for low-reach accounts, Tier 2 requires private identity verification for moderate-influence users, and Tier 3 mandates independent fact-checking for mass-reach content. The authors use Reddit's community moderation as evidence that tiered governance emerges organically and is operationally feasible. They outline regulatory pathways through existing EU Digital Services Act, UK Online Safety Act, and evolving US jurisprudence to implement reach-proportional identity verification while preserving privacy for ordinary users.

### Strengths
The paper tackles a genuinely important problem with a novel, proportionate solution that avoids the extremes of blanket anonymity or universal real-name requirements. The Reddit empirical evidence effectively demonstrates organic emergence of tiered governance. The cross-jurisdictional regulatory analysis is thorough and identifies concrete implementation pathways. The technical framework is detailed yet feasible, building on existing platform capabilities.

### Weaknesses
The definition of "reach" and threshold calibration remains underdeveloped - critical implementation details that could determine success or failure. The paper underestimates enforcement challenges, particularly regarding jurisdiction shopping and technical circumvention. The assumption that platforms will comply without significant resistance may be overly optimistic. Limited analysis of how authoritarian regimes might exploit these frameworks for censorship purposes.

### Questions
How would you address the fundamental challenge of defining and measuring "reach" consistently across platforms with different engagement models? What specific safeguards would prevent authoritarian governments from exploiting tiered identity requirements for political suppression? How might the framework adapt to emerging platforms or communication technologies that don't fit traditional social media models? What evidence suggests that fact-checking requirements for Tier 3 users would be more effective than current voluntary approaches?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues for governments to institute a tiered approach to user anonymity for social media platforms that would assign user accounts to one of three tiers, with progressively stricter accountability requirements.  The goal is to reduce the proliferation of deepfakes and misinformation.  The tiers are assigned based on a user's "reach" (sum of followers, shares, views, and other elements of influence).  Observations of Reddit norms are used to support the proposed framework.  The paper also demonstrates how the proposal is consistent with existing legislation in the EU and U.K. and some elements of U.S. legislation.

### Strengths
The paper makes a clear argument for the need for tiered anonymization for users of digital platforms.  This is a particularly compelling statement: "Ultimately, tiered anonymity is not about censoring speech – it is about regulating amplification" (line 366). Rather than burying it at the end of section 8, this could be a strong way to lead the reader into the idea (since most first reactions will involve a concern about the suppression of free speech).

The strongest part of the paper is its grounding in legal and regulatory contexts in the EU, U.K., and U.S. (Section 4) and globally (the first part of section 7).

The topic is very relevant to the social media and online platform communities.  It is less clear that it relates strongly to the NeurIPS (machine learning and computational neuroscience) communities.  Still, it is likely to inspire debate and discussion.

Suggestion:
1. It would help to explain to reader what "shield" section 230 provides since not everyone is familiar with it.

### Weaknesses
(1) The Reddit evidence is weak. The claim that strict rules naturally occur with increasing subreddit sizes (lines 104-106) should be supported with data relating subreddit size to a measure of "friction". The claim that Reddit’s system scales "without eroding baseline pseudonymity" is unsupported. Lines 107-108: "High-visibility communities even demand identity proofs" which must erode pseudonymity.

(2) The paper does not demonstrate that governments are the right agents to act. Any restriction on speech by the U.S. government invites constitutional challenges, despite the claim that the proposal is "constitutionally sound" (lines 254-255). Platform action or industry standards would avoid that challenge. No such alternatives (or others) are addressed.

Suggestions:

1. Define "pseudonymity".

2. The paper states that it "restores proportionate friction to digital speech" (lines 62-63), but it does not show that there ever was "proportionate friction" in the past, so it cannot be "restored". Online anonymity has been part of the Internet since early on; see e.g. the "on the Internet, nobody knows you're a dog" cartoon from the New Yorker in 1993.

3. The U.S. Take It Down Act (May 2025) relates to Section 5.3 (lines 249-253).

### Questions
The scope of this paper seems to be global, encouraging all governments to employ a tiered anonymity system.  Is the intent that all countries would work to identify the same tiered anonymity system (for consistency)?  If not, wouldn't the proposal face the same fragmentation challenges discussed in section 8?  Lines 348-353 seem to dance around this issue by calling for "cooperation" and aiming for "harmonization" but not coming out and stating that the same tiers should be used everywhere.  Therefore the intent is not clear.

### Presentation
4

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces a meta-protocol (called \pname{}) for communication between LLM-powered agents. The protocol sidesteps the "Agent Communication Trilemma" (versatility vs. efficiency vs. portability) by using a hybrid approach: human-written routines for frequent communications, LLM-written routines for intermediate-frequency communications, and natural language for rare or fallback cases. Protocol Documents (PDs), identified by hash, are negotiated and shared autonomously by agents. The paper demonstrates the approach with a two-agent weather data exchange and a 100-agent network handling 1,000 queries, reporting a ~5× cost reduction versus natural-language-only communication.

## Strengths

- **Measurable cost reduction in a non-trivial multi-agent setup.** The 100-agent demo (Section 5.3) runs 1,000 queries across agents using heterogeneous LLMs (GPT-4o, Llama-3-405B, Gemini 1.5 Pro) and databases (SQL, MongoDB), achieving a cost of $7.67 USD versus $36.23 USD for natural-language-only communication (~4.7× improvement, Figure 2a). This directly supports the efficiency claim.

- **Autonomous protocol negotiation without human intervention.** In the two-agent demo (Section 5.2), agents independently negotiate a structured JSON protocol for weather data (fields for location, date, temperature, precipitation, condition) and each writes its own routine. The paper states "the entire communication happened without human intervention" — a clear differentiation from hand-coded API integrations.

- **Hash-based protocol identification enables full decentralization.** Protocol documents are identified by their content hash (Section 5.1), removing the need for a central registry. The paper demonstrates this works across heterogeneous agents in the 100-agent demo and notes compatibility with IPFS and other decentralized storage.

- **Formalization of the Agent Communication Trilemma.** Section 3 provides a clear conceptual framing of the three-way trade-off between versatility, efficiency, and portability. This gives the paper's design a principled motivation that is absent from much multi-agent LLM work, where communication choices are made ad hoc.

## Weaknesses

### Fatal

None. The paper's core concept — a hybrid adaptive protocol with three tiers of communication — is sound, and the demo provides proof-of-concept evidence that the approach works and saves costs.

### Major

1. **Method is specified only at a conceptual level, lacking the precision needed for reproducibility.** The paper describes the protocol flow in prose (negotiation → PD hash lookup → routine generation → fallback) but provides no pseudocode, state machine, message-type enumeration, or formal specification in the main text. Key operational questions remain unanswered: What is the exact sequence of message types during negotiation? How does an agent detect that a routine "fails" and trigger the natural-language fallback? What mandatory fields must a PD contain (beyond being a "plain-text description")? The paper references an appendix for a "more formal description," but the main text itself lacks the specificity expected for a claimed protocol contribution. This is the most significant weakness because it prevents other researchers from building on or reproducing the work.

2. **The evaluation does not support the strongest claims ("unprecedented scalability," emergent self-organizing protocols").** The 100-agent experiment is a single run with 1,000 queries. There is no:
   - Failure or success rate analysis (how many queries were completed successfully? Did any require human intervention?).
   - Measurement of how communications distributed across the three tiers (human-written routine vs. LLM-written routine vs. natural language) and how this distribution evolved.
   - Analysis of scalability beyond 100 agents (latency, throughput, bandwidth, or behavior under agent churn).
   - Error bars or variance in the cost comparison (the cost plot shows a smoothed line with window size 100 but no confidence intervals).
   
   The "unprecedented scalability" claim in the abstract and conclusions is not supported by a single 100-agent run. The "emergent protocols" claim rests on one qualitative example (food delivery) without quantitative tracking of how many PDs were negotiated, how many agents adopted each, or whether reuse increased over time.

3. **No experimental comparison against existing multi-agent LLM approaches.** The paper positions \pname{} as a solution to a problem shared by all multi-agent LLM systems, and cites works such as MetaGPT and CAMEL in related work, but the only baseline is natural-language-only communication. Without comparison to how these or similar frameworks handle the same tasks under similar conditions, it is impossible to assess whether \pname{} offers an improvement over the state of the art or is merely a re-description of known hybrid approaches.

4. **Cost analysis is not fully transparent.** The paper reports a $0.043 negotiation cost for the two-agent demo (Section 5.2) and $7.67 total for the 100-agent demo, but does not disclose: the number of messages exchanged during any single negotiation, the token counts for LLM calls, the specific model used for each negotiation phase (agents use different LLMs — which handled the protocol negotiation?), or the cost of LLM-written routine generation separately from routine execution. This makes it difficult to verify or extend the cost analysis.

### Minor

- The negotiation success condition is under-specified. Section 5.1 describes a mechanism where agents expose supported protocols via endpoints and compare lists, but also says negotiation happens "after a few rounds." It is unclear whether negotiation is a structured exchange (enumeration of capabilities, proposal, counter-proposal, acceptance) or free-form natural language until agreement. The paper would benefit from clarifying the negotiation protocol itself.

- The "backward compatibility" claim (Section 4, Section 5.1) asserts that existing protocols like OpenAPI can be used as PDs, but does not address the practical challenge that these schemas are not designed to be parsed by LLMs into executable routines. This claim needs further justification or experimental demonstration.

- The Trilemma is presented qualitatively without operationalizing any of the three axes. While useful as a framing device, the paper never quantifies versatility, efficiency, or portability, making the claim of "sidestepping" the Trilemma a conceptual argument rather than a measured one.

### Trivial

- The paper's name is consistently rendered as `\pname{}` in the source, a placeholder that survives into the extracted text. This is a parser artifact and not relevant to scientific evaluation.

## Nice-to-Haves

- An ablation study testing what happens when only two of the three tiers are used (e.g., only human-written routines + natural language without LLM-written routines) would clarify which component drives the cost savings.
- A failure analysis quantifying how often LLM-written routines break and how often the natural-language fallback is triggered would strengthen the robustness claims.
- Measuring human setup effort (e.g., person-hours to configure the 100-agent network) would substantiate the portability claim.

## Removed Points

- **Criticism about missing appendix content** (the paper referencing an appendix for formal details): Parser strips appendix sections from all papers; the original submission contains this material. Removed per hard rule.
- **Criticism that the hybrid approach is "obvious" or "not a deep insight"**: This is a subjective opinion about novelty, not an identifiable flaw in the paper's content. Removed.
- **Criticism about hash collisions and versioning**: While technically a concern, the hash-based identification is a standard practice (content-addressing), and versioning is a general engineering concern applicable to any protocol, not a specific weakness of this paper's contribution. Demoted to removed.
- **Strength Finder strengths that are generic** ("this paper addressed an important problem"): Removed as superficial; only concrete, evidence-backed strengths retained.
- **Criticism that the Trilemma is "oversimplified" and a "rhetorical device"**: This is a subjective framing critique. The Trilemma's qualitative nature is acknowledged as a minor weakness above; the stronger dismissive characterization is removed.

## Novel Insights

The two reviews together surface an important tension that the paper itself does not fully confront: the protocol is simultaneously the paper's main contribution and its weakest-supported component. The Trilemma framing and hash-based PD design are genuinely thoughtful, but the paper stops at the conceptual+proof-of-concept stage when the subject matter demands specification rigor equivalent to what a protocol RFC would provide. The cost savings are real but stem almost entirely from the well-known observation that structured API calls are cheaper than LLM inference — the paper's novelty lies in making agents *autonomously discover and adopt* those API-like structures, which is a research contribution worth taking seriously. The gap between the paper's vision and its execution is bridgeable, but requires either (a) scaling back the claims to match the current evidence, or (b) substantially expanding both the specification and the evaluation.

## Suggestions

1. **Add a formal protocol specification in the main text** — at minimum, pseudocode for the negotiation loop, the message envelope format, the PD hash lookup, the routine generation trigger condition, and the fallback state machine. This is the single most impactful change.
2. **Replace "unprecedented scalability" with scoped claims** about cost efficiency and autonomous protocol negotiation in networks of up to 100 agents, supported by quantitative tier-usage data.
3. **Add success-rate and failure-mode metrics** to the 100-agent evaluation (how many queries completed, how many required LLM fallback, how many failed completely).
4. **Benchmark against at least one existing multi-agent framework** on the same task or a standardized subset, even if the comparison is limited to cost and completion rate.
5. **Disclose token counts and per-phase cost breakdowns** for both demos to make the cost analysis independently verifiable.

## Summary

This paper is a point-by-point rebuttal to a TPAMI response paper (Palazzo et al., 2024), defending the work of Bharadwaj et al. (2023) and Ahmed et al. (2021) against a series of criticisms. It argues that approximately 100 published papers relying on block-design EEG datasets suffer from a temporal confound — a correlation between stimulus class and time-within-run — that inflates classification accuracy. The paper addresses seven specific claims from Palazzo et al. (2024), labeling each as false, misleading, unfounded, or inaccurate, and presents one new experiment (frequency-domain supertrial averaging) to rebut a claim about signal attenuation.

## Strengths

- **Concrete identification and rebuttal of specific technical errors**: Each claim is confronted with direct quotations from the opposing work and counter-evidence. The rebuttal of the "signal bleeding" claim (Section 2) is well-grounded: the contested dataset used 2 s stimulus duration with 1 s inter-trial blanking, which is materially different from the 0.5 s no-blanking designs where bleeding is plausible.

- **New experimental evidence in Section 7**: The frequency-domain supertrial experiment (FFT-based amplitude/phase averaging) directly addresses Palazzo et al.'s claim that time-domain averaging necessarily attenuates high-frequency content. Table 1 reproduces above-chance accuracy for SVM, 1D CNN, EEGNet, and SyncNet while EEGChannelNet remains at chance — validating the core empirical claim of Bharadwaj et al. (2023) under an alternative averaging scheme.

- **Important scientific integrity argument**: The ethics statement correctly characterizes a systemic problem — that datasets with embedded temporal clocks allow inflated performance that cannot be distinguished from genuine EEG decoding, with downstream harms to grants, publications, and medical applications.

- **Logical rebuttal of the "proving a negative" fallacy**: Section 8 appropriately points out that failing to detect the confound in a sub-analysis (blank-screen classification) does not establish the absence of the confound, and further shows that Palazzo et al.'s BDB analysis targets a different (between-run) confound than the within-run confound actually at issue in Li et al. (2021).

## Weaknesses

### Fatal
None that invalidate the paper's specific technical rebuttals.

### Major

- **The paper is not a standalone research contribution; it is a reactive dispute commentary.** Every section is structured as "Palazzo et al. claim X; X is false because…." The single new scientific contribution — frequency-domain supertrials — is one page of analysis and one table. For an ICLR submission, the paper lacks an independent research question, a methodology presented on its own merits, or results that advance the state of knowledge beyond defending prior work. The paper's value is entirely contingent on the reader being deeply familiar with Bharadwaj et al. (2023), Ahmed et al. (2021), Li et al. (2021), and Palazzo et al. (2020b; 2024).

- **The broader argument about ~100 confounded papers is made by citation, not by demonstration.** The claim that nearly 100 papers are flawed is listed in the ethics statement with a block citation but no analysis in the current paper. The evidence for the temporal confound was established in Li et al. (2021) and Bharadwaj et al. (2023); this paper does not extend, update, or strengthen that evidence beyond one supplementary experiment.

- **No generalization or methodological contribution.** The paper does not explain to the ICLR community how to detect this class of confound, how to design EEG experiments to avoid it, or what the positive path forward looks like. It is fully backward-looking.

### Minor

- The leave-one-subject-out analysis cited in Section 8 (Li et al., 2021, Table 8) to counter the pooling argument is referenced but not reproduced or extended, leaving the empirical argument reliant on the reader trusting a prior paper.

- Figure 1 description notes that spectra "generally trend downward as frequency increases" for all conditions including raw trials; clarification of why frequency-domain averaging amplifies high frequencies (as claimed in the text) would strengthen the argument.

### Trivial
None identified.

## Nice-to-Haves

- A concise positive summary of what constitutes a methodologically sound EEG visual decoding experiment would add value for readers not deeply embedded in this literature.
- Extending Table 1 to the six-subject Li et al. (2021) data (right half of Bharadwaj et al. 2023, Table 1) under frequency-domain supertrials would strengthen the cross-subject generalization claim.

## Novel Insights

The frequency-domain supertrial construction (FFT averaging of magnitude and phase independently) is a useful methodological note: it shows that the low-pass character of time-domain averaging is not fundamental to the supertrial concept and that phase-preserving frequency-domain alternatives maintain high-frequency content. This reframes the supertrial approach as more flexible than critics assumed. Beyond that, however, the paper does not produce new scientific insights — it defends and clarifies existing ones.

## Suggestions

- Reframe the paper as a standalone methods/empirical study that (a) introduces frequency-domain supertrials as a formal technique, (b) provides a comprehensive characterization of confound types in EEG block-design experiments, and (c) gives practical guidance for experiment design. This would transform the reactive commentary into a genuinely standalone ICLR contribution.
- Add a prospective section: what classification accuracy is achievable on nonconfounded EEG data today, and what does this tell us about the ceiling of the task?

## Score and Decision

This paper makes technically correct and scientifically important points. Its core thesis — that Palazzo et al. (2024) mischaracterize the methodology of prior work and that the temporal confound in block-design EEG datasets is real and severe — is well-supported within the text. The one new experiment is sound. However, as an ICLR submission it is structurally and substantively a dispute commentary, not a research paper. It offers no novel method, no new dataset, no new empirical study of meaningful scope, and no theoretical advance. Its value is real but narrowly situated within a TPAMI exchange that most ICLR readers will not be following. The paper would be more appropriate as a response/comment published at the venue where the original dispute lives (TPAMI), or as a component of a larger, standalone paper on confound detection and correction in EEG decoding.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>
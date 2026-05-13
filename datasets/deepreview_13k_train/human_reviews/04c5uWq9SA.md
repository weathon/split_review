# A False Sense of Privacy: Evaluating Textual Data Sanitization Beyond Surface-level Privacy Leakage

- Decision: Reject
- Scores: 8, 5, 5, 5

## Abstract
The release of sensitive data often relies on synthetic data generation and Personally Identifiable Information~(PII) removal, with an inherent assumption that these techniques ensure privacy. However, the effectiveness of sanitization methods for text datasets has not been thoroughly evaluated. To address this critical gap, we propose the first privacy evaluation framework for the release of sanitized textual datasets. In our framework, a sparse retriever initially links sanitized records with target individuals based on known auxiliary information. Subsequently, semantic matching quantifies the extent of additional information that can be inferred about these individuals from the matched records. We apply our framework to two datasets: MedQA, containing medical records, and WildChat, comprising individual conversations with ChatGPT. Our results demonstrate that seemingly innocuous auxiliary information, such as specific speech patterns, can be used to deduce personal attributes like age or substance use history from the synthesized dataset.
We show that private information can persist in sanitized records at a semantic level, even in synthetic data. Our findings highlight that current data sanitization methods create a false sense of privacy by making only surface-level textual manipulations. This underscores the urgent need for more robust protection methods that address semantic-level information leakage.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The manuscript seeks to highlight privacy concerns in text-sanitization techniques, by a) proposing a semantic-similarity based privacy metric for re-identification/matching attacks, and b) evaluating state-of-the-art defenses against such inference under the proposed metric. 

The authors use a 2-step approach; in the first 'linking' step, sanitized documents are compared to externally known auxiliary information about a target individual using a TFIDF-based sparse retriever, and in the second 'semantic matching' step, a language model is used to assess similarity between atomic claims in the retrieved document and those in the original, unsanitized document.

The paper then evaluates several defense strategies to quantify information leakage under the above framework, and find that DP based methods may provide some of the strongest protections, albeit at the cost of data utility.

### Strengths
- Extremely well-written paper, with clear motivation and research questions.
- The figures in the paper are very informative, and do an excellent job of conveying key information. The running examples were great for readability.
- Clear problem statement, with adequate background and justification of design choices. Creative use of LLMs as an evaluation for text-coherence.
- The results about access to different sets of auxiliary information were really interesting to me. The hypothesis about the non-uniformity of LLMs' instruction-following seems intuitive, but would be interesting to quantify this in its own right.
- The human subject experiments were a nice touch - useful to know the capabilities of the two models in this context.

### Weaknesses
Can't think of any immediate flaws or weaknesses. Happy to discuss further once other reviews are in.

### Questions
- Did you find major differences between the two datasets in terms of atomizing claims in documents? It seems to me that this would be more structured in a medical Q&A dataset, as compared to LLM-user interactions.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a framework to evaluate sanitization methods for releasing datasets with textual data. They highlight that obvious methods such as removing explicit identifiers like names is insufficient for properly protecting privacy, since other semantic details can also leak private information. Also, auxiliary information about an individual may be linkable to a supposedly sanitized target document, thus allowing an attacker to infer or recover further sensitive details.

The goal of the framework is the quantification of information leakage from sanitized documents given auxiliary information about the document's owner or author.
The framework proposes to determine auxiliary information from each original documents by extracting individual "claims". For each document, the attacker is given a subset of claims and runs a sparse retriever to find the best-matching document from the set of sanitized documents.
They then define a similarity metric, which is either determined by an LLM or the ROGUE-L score, to compute the similarity between the retrieved document and the remaining claims extracted from the original document.
Additionally, they define task-specific utility metrics for each evaluated dataset.

In the evaluation, the authors consider two datasets: MedQA from the medical domain with a question-answering task, as well as WildChat consisting of online conversations with ChatGPT and a text categorization task. They also consider a range of sanitization methods that either work by removing PII or by generating synthetic data, the latter also with the option of providing differential privacy.
In each scenario, the newly introduced semantic and lexical privacy metrics are computed, along with task-specific utility measures as well as the quality (coherence) of the sanitized texts. Lastly, they perform a human evaluation to determine which variant of the privacy metric best matches  human preferences.

### Strengths
Formalizing linkage attacks for unstructured text data is a nice and useful contribution, and enables a systematic evaluation of various (novel) text sanitization methods in the future.

While not entirely new, cf. e.g., [1] and the already cited (Stadler et al., 2022), the observations that superficial sanitization methods (such as PII removal) are often insufficient to properly protect privacy remains important.

For most parts, the paper is well written and easy to follow. However, there are some uncertainties about metrics and inconsistencies between numbers reported in the texts and tables, which are (in my view) confusing to the reader and undermine the validity of the currently reported results.

### Weaknesses
I stumbled across some inconsistencies between the numbers reported in the Tables and discussed in the text. Please double-check (cf. questions) and update, or explain the differences.

Some details about the metrics and their computation remain unclear (cf. questions). Please try to use consistent naming and define concepts (such as the definition of metrics/distances) in one concise and consecutive piece of text (not spread across several sections).

L323: I think the conclusion from a "disparity between lexical and semantic similarity" to "these techniques primarily modify and paraphrase text without effectively disrupting the underlying connected features and attributes" is made a bit prematurely: Both are entirely different measures, and even for "no sanitization", the lexical score is twice the semantic score. Also, what would happen if you shifted the (apart from the ordering: somewhat arbitrarily) assigned scores for the "similarity metric" in Section 2.4 from {1,2,3} to {0,1,2} or to {1,10,100}?

L081, L099: Just to be sure: If I understood correctly, "claims" can refer to any sensitive or non-sensitive information in the original texts?

L101: If (1) PII removal had 94% leakage (inferable claims), and (2) data synthesis (with or without DP?) has 9% lower leakage (i.e., 85% ?), why does (3) data synthesis without DP state 57% << 85% leakage?

Section 2.3 Linking Method:
- L146: Could you briefly motivate the use of the sparse BM25 retriever? Did you consider dense retrieval methods (say, using some form of text embeddings)? What are the benefits of BM25 vs. other sparse methods, or of sparse methods vs. dense methods, in particular for the linkage task at hand?
- L147-148: You state your "approach aggregates the auxiliary information into a single text chunk" -- Does that mean you combine (concatenate?) _all_ "atomized claims" x^(i)_j across all j into the "aux info" {\tilde x}^(i)? (Wouldn't hurt to write this down more explicitly.) (Just found the info in L296/Section 3.3 that the attacker gets 3 random claims for the linkage phase. I find that a bit late, it would be better to mention it directly in Section 2.3 to avoid confusion/guessing on the side of the reader.)

Section 2.4 Similarity Metric:
- L156: Can you give a specific reason for querying only with claims that were _not_ utilized in the linking phase? Besides, how do I know whether a claim about an original document was used for linking? If _all_ atomized claims are combined into the aux info (cf. previous question), and the aux info is used as query in the retriever, wouldn't this imply that all claims are already consumed in the linking phase?
- L159: If I understood correctly, you define the "similarity metric" µ between the original and linked documents by querying a language model to judge the document similarity, where you assign values on a scale from 1 (for 'identical documents') to 3. I wonder if it would make more sense to start the scale at 0, since mathematically, a metric has the property of evaluating to 0 for identical inputs. (In your case, we would get "µ(x,x) > 0" instead of "µ(x,x) = 0".)
- How do I know that the atomized claims, which are used to compute µ and hence to measure privacy preservation, are actually privacy-relevant, and not just some arbitrary, privacy-*in*sensitive facts?

L313: I'm confused regarding the symbol "µ" seemingly used for multiple purposes. It is defined in Sec. 2.4, but here, you also use it for another metric induced by ROGUE-L scores.

L317 (also L386): You state "zero-shot prompting achieves an accuracy of 0.44" for MedQA task utility, but why am I unable to find that result in Table 1 (for "No Sanitization", it says 0.69)?

Table 1:
- Calling the privacy metrics "Overlap" and "Similarity" is very confusing, since they actually mean the opposite (high lexical overlap and semantic similarity would indicate a high agreement between the two documents, but high scores in Table 1 mean good privacy). Name them lexical/semantic "distance" instead?
- Talking about metrics: In Equation 1 you define a "privacy metric", I guess that is what is reported under the (why differently named?) "Semantic Similarity" column in Table 1. It is based on the "similarity metric" from Section 2.4, which has values between 1 and 3 -- How does it end up with values between 0 and 1 in Table 1?? I couldn't see any discussion on some form of normalization of these scores. The expected value of scores >= 1 in Eq. 1 would still result in a value >= 1, and not in [0,1). Please double-check how you actually compute the metrics. Try *not* to distribute information pertaining to one concept across the paper, but put it concisely into one place if possible. Also prefer consistent naming.

Table 2:
- The effect of \epsilon appears surprisingly small to me, with only minimal changes across all metrics even when comparing \epsilon=3 and 1024. Can you explain this behavior?
- It would be interesting to compare with a random baseline where the utility is determined from completely random texts -- to rule out that 0.4x task utility in the case of MedQA can already be achieved based on completely random input (say, if the dataset suffers from strong class imbalance and the classifier always just guesses the largest class, thus obtaining an overly optimistic accuracy).

Table 3:
- L404: What exactly is the "linkage rate"? Please specify.
- L423: Contradicting statements: Here, you state the last three claims are used, previously in L296, you mentioned 3 randomly selected claims.

L443/Section 2.4: If you can switch the similarity metric µ also to ROGUE-L, please already state this as possible option in Section 2.4 where you introduce µ. Currently, you only say there that µ is determined by querying a language model.

Lastly, what are your thoughts on information that is both privacy-sensitive and utility-relevant, say, if one or more atomized claims are also strongly related to a downstream task? For instance, what if an atomized claim turns out to be "John likes baseball", and one of the WildChat categories is "baseball", too? Feel free to substitute "baseball" with something more delicate, such as "drinking alcohol".
(Case A: If the baseball aspect is kept in the sanitized document, both µ and the chi^2 distance should be small, indicating poor privacy but good utility. Case B: If the baseball aspect was redacted, both µ and chi^2 should be larger, indicating better privacy but poorer utility.)

Additional considerations for related work:
[1] also highlights the insufficiencies of superficial sanitization methods for text. [1] and also [3,4,5] propose differentially private methods that obfuscate texts. An evaluation framework for text rewriting has also been introduced previously [6].
[2] has been published in parallel with (Yue et al., 2023) and also suggests differentially private synthetic text generation.
- [1] Weggenmann & Kerschbaum, "SynTF: Synthetic and Differentially Private Term Frequency Vectors for Privacy-Preserving Text Mining", SIGIR 2018
- [2] Mattern et al., "Differentially Private Language Models for Secure Data Sharing", EMNLP 2022
- [3] Weggenmann et al. "DP-VAE: Human-Readable Text Anonymization for Online Reviews with Differentially Private Variational Autoencoders", WWW 2022
- [4] Igamberdiev & Habernal, "DP-BART for Privatized Text Rewriting under Local Differential Privacy", ACL Findings 2023
- [5] Bo et al., "ER-AE: Differentially Private Text Generation for Authorship Anonymization", NAACL 2019
- [6] Igamberdiev et al. "DP-Rewrite: Towards Reproducibility and Transparency in Differentially Private Text Rewriting", COLING 2022

### Questions
L081, L099: Just to be sure: If I understood correctly, "claims" can refer to any sensitive or non-sensitive information in the original texts?

L101: If (1) PII removal had 94% leakage (inferable claims), and (2) data synthesis (with or without DP?) has 9% lower leakage (i.e., 85% ?), why does (3) data synthesis without DP state 57% << 85% leakage?

Section 2.3 Linking Method:
- L146: Could you briefly motivate the use of the sparse BM25 retriever? Did you consider dense retrieval methods (say, using some form of text embeddings)? What are the benefits of BM25 vs. other sparse methods, or of sparse methods vs. dense methods, in particular for the linkage task at hand?
- L147-148: You state your "approach aggregates the auxiliary information into a single text chunk" -- Does that mean you combine (concatenate?) _all_ "atomized claims" x^(i)_j across all j into the "aux info" {\tilde x}^(i)? (Wouldn't hurt to write this down more explicitly.) (Just found the info in L296/Section 3.3 that the attacker gets 3 random claims for the linkage phase. I find that a bit late, it would be better to mention it directly in Section 2.3 to avoid confusion/guessing on the side of the reader.)

Section 2.4 Similarity Metric:
- L156: Can you give a specific reason for querying only with claims that were _not_ utilized in the linking phase? Besides, how do I know whether a claim about an original document was used for linking? If _all_ atomized claims are combined into the aux info (cf. previous question), and the aux info is used as query in the retriever, wouldn't this imply that all claims are already consumed in the linking phase?
- L159: If I understood correctly, you define the "similarity metric" µ between the original and linked documents by querying a language model to judge the document similarity, where you assign values on a scale from 1 (for 'identical documents') to 3. I wonder if it would make more sense to start the scale at 0, since mathematically, a metric has the property of evaluating to 0 for identical inputs. (In your case, we would get "µ(x,x) > 0" instead of "µ(x,x) = 0".)
- How do I know that the atomized claims, which are used to compute µ and hence to measure privacy preservation, are actually privacy-relevant, and not just some arbitrary, privacy-*in*sensitive facts?

L313: I'm confused regarding the symbol "µ" seemingly used for multiple purposes. It is defined in Sec. 2.4, but here, you also use it for another metric induced by ROGUE-L scores.

L317 (also L386): You state "zero-shot prompting achieves an accuracy of 0.44" for MedQA task utility, but why am I unable to find that result in Table 1 (for "No Sanitization", it says 0.69)?

Table 1:
- Calling the privacy metrics "Overlap" and "Similarity" is very confusing, since they actually mean the opposite (high lexical overlap and semantic similarity would indicate a high agreement between the two documents, but high scores in Table 1 mean good privacy). Name them lexical/semantic "distance" instead?
- Talking about metrics: In Equation 1 you define a "privacy metric", I guess that is what is reported under the (why differently named?) "Semantic Similarity" column in Table 1. It is based on the "similarity metric" from Section 2.4, which has values between 1 and 3 -- How does it end up with values between 0 and 1 in Table 1?? I couldn't see any discussion on some form of normalization of these scores. The expected value of scores >= 1 in Eq. 1 would still result in a value >= 1, and not in [0,1). Please double-check how you actually compute the metrics. Try *not* to distribute information pertaining to one concept across the paper, but put it concisely into one place if possible. Also prefer consistent naming.

Table 2:
- The effect of \epsilon appears surprisingly small to me, with only minimal changes across all metrics even when comparing \epsilon=3 and 1024. Can you explain this behavior?
- It would be interesting to compare with a random baseline where the utility is determined from completely random texts -- to rule out that 0.4x task utility in the case of MedQA can already be achieved based on completely random input (say, if the dataset suffers from strong class imbalance and the classifier always just guesses the largest class, thus obtaining an overly optimistic accuracy).

Table 3:
- L404: What exactly is the "linkage rate"? Please specify.
- L423: Contradicting statements: Here, you state the last three claims are used, previously in L296, you mentioned 3 randomly selected claims.

L443/Section 2.4: If you can switch the similarity metric µ also to ROGUE-L, please already state this as possible option in Section 2.4 where you introduce µ. Currently, you only say there that µ is determined by querying a language model.

Lastly, what are your thoughts on information that is both privacy-sensitive and utility-relevant, say, if one or more atomized claims are also strongly related to a downstream task? For instance, what if an atomized claim turns out to be "John likes baseball", and one of the WildChat categories is "baseball", too? Feel free to substitute "baseball" with something more delicate, such as "drinking alcohol".
(Case A: If the baseball aspect is kept in the sanitized document, both µ and the chi^2 distance should be small, indicating poor privacy but good utility. Case B: If the baseball aspect was redacted, both µ and chi^2 should be larger, indicating better privacy but poorer utility.)

Additional considerations for related work:
[1] also highlights the insufficiencies of superficial sanitization methods for text. [1] and also [3,4,5] propose differentially private methods that obfuscate texts. An evaluation framework for text rewriting has also been introduced previously [6].
[2] has been published in parallel with (Yue et al., 2023) and also suggests differentially private synthetic text generation.
- [1] Weggenmann & Kerschbaum, "SynTF: Synthetic and Differentially Private Term Frequency Vectors for Privacy-Preserving Text Mining", SIGIR 2018
- [2] Mattern et al., "Differentially Private Language Models for Secure Data Sharing", EMNLP 2022
- [3] Weggenmann et al. "DP-VAE: Human-Readable Text Anonymization for Online Reviews with Differentially Private Variational Autoencoders", WWW 2022
- [4] Igamberdiev & Habernal, "DP-BART for Privatized Text Rewriting under Local Differential Privacy", ACL Findings 2023
- [5] Bo et al., "ER-AE: Differentially Private Text Generation for Authorship Anonymization", NAACL 2019
- [6] Igamberdiev et al. "DP-Rewrite: Towards Reproducibility and Transparency in Differentially Private Text Rewriting", COLING 2022

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a privacy evaluation framework for data sanitization methods, specifically data anonymization and data synthesis, in the context of natural language. The framework can be summarized as follows: first, random records from the original data are sampled as the auxiliary data; then, an information retrieval technique is used to link the auxiliary data with the sanitized data, and an LLM is utilized to evaluate the semantic similarity between the original records and the linked records. The final similarity scores denote the degree of privacy leakage of the sanitized data.

### Strengths
This paper focuses on the privacy leakage of text data. The authors design different prompts for LLM to evaluate the semantic similarity between two sentences, which is interesting. The experimental results are extensive. Multiple data sanitization techniques are included in the evaluation framework.

### Weaknesses
1. The main issue of this paper is the definition of privacy leakage, which the authors equate with semantic similarity between auxiliary data and sanitized data. However, the semantic information of a sentence reflects its utility. If the semantic content of a sanitized sentence is altered, the sanitization method would be useless. Traditional data anonymization methods aim to remove only identifiers from a data record rather than all information. In this context, identifiers should be the privacy focus, and privacy leakage should refer specifically to identifier leakage.

2. The technical novelty is relatively limited. The linking step uses the existing BM25 retriever, while the semantic similarity evaluation mainly relies on established prompt engineering techniques.

3. The findings are not particularly interesting, as it is well-known that simple data anonymization and data synthesis techniques are insufficient to protect data privacy. This paper's findings merely confirm that this limitation also applies to text data.

4. The numerical results rely on LLM output, which is relatively qualitative and less persuasive. Additionally, querying LLaMA three times for consistency seems unnecessary; disabling sampling parameters in text generation should ensure consistent results from LLaMA for the same query.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the current limitations of existing textual data sanitization methods. By considering re-identification attacks with known auxiliary information, the paper shows that a sparse retriever can link sanitized records with target individuals even though the PII patterns are anonymized. Instead, the paper proposes a new privacy evaluation framework for the release of sanitized textual datasets. The paper considers two datasets, including MedQA and WildChat, to show that seemingly innocuous auxiliary information can be used to deduce personal attributes like age or substance use history from the synthesized dataset. Experimental results also verify that current data sanitization methods create a false sense of privacy only on the surface level.

### Strengths
1. The paper is well-written and easy to follow. All the included sanitization methods are up-to-date and well-explained.

2. The proposed method is straightforward in decomposing the re-identification with linking and matching methods. 

3. Experimental results are comprehensive with sufficient ablation experiments. The included baselines are solid and up-to-date.

### Weaknesses
1. My major concern is that the auxiliary data is highly contrived. Based on my understanding, each auxiliary sample is the subset of exact atomics from the target record. For example, in Fig 1, Auxiliary Information contains two atoms of the Original Record. That is, if you only consider de-identified, sanitized records, it is very easy for your BM25 retriever to get the sanitized target. In real-world re-identification attacks, there is no such auxiliary information that has many exact overlapped n-grams as original records. 

2. For the claim that 'private information can persist in sanitized records at a semantic level, even in synthetic data,' if you consider DP generation, the privacy level is indicated by $(\epsilon, \delta)$. That is, your linked record may not be the original target sample. DP introduces random noise to offer plausible deniability and protect the original record's privacy.

3. The implemented methods for the proposed privacy evaluation framework only integrate various existing components by using the contrived auxiliary data. It is not likely to scale this framework for a large number of overlapped atoms.

### Questions
Please refer to my weaknesses. Also, I have a few new questions.

1) How can your method extend to other datasets? Is there any real auxiliary data that can be used instead of creating overlapped auxiliary data from the original records?

2) Regarding the concept of privacy, is converting the age of 23 to early 20s a privacy breach? Such conversion is commonly adopted by K-anonymity.

### Soundness
2

### Presentation
3

### Contribution
3

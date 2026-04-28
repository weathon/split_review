# Process-Driven Autoformalization in Lean 4

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 1, 8

## Abstract
Autoformalization, the conversion of natural language mathematics into formal languages, offers significant potential for advancing mathematical reasoning. However, existing efforts are limited to formal languages with substantial online corpora and struggle to keep pace with rapidly evolving languages like Lean 4. To bridge this gap, we propose a large-scale dataset \textbf{Form}alization for \textbf{L}ean~\textbf{4} (\textbf{\dataset}) designed to comprehensively evaluate the autoformalization capabilities of large language models (LLMs), encompassing both statements and proofs in natural and formal languages. Additionally, we introduce the
\textbf{P}rocess-\textbf{D}riven \textbf{A}utoformalization (\textbf{\method}) framework
that leverages the precise feedback from Lean 4 compilers to enhance autoformalization. 
Extensive experiments demonstrate that \method improves autoformalization, enabling higher compiler accuracy and human-evaluation scores using less filtered training data. 
Moreover, when fine-tuned with data containing detailed process information, \method exhibits enhanced data utilization, resulting in more substantial improvements in autoformalization for Lean 4.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a new dataset FormL4 for evaluating autoformalization in Lean4. The paper also proposes a framework called PDA to improve autoformalization capabilities of LLMs.

### Strengths
The introduced dataset would be useful for LLM-based auto formalization research
- The evaluation is comprehensive and uses human evaluation for autoformalizer performance

### Weaknesses
 - Line 103: One of the contributions states that - “We propose a process-driven framework PDA that leverages formal languages to provide process feedback on reasoning, enhancing the autoformalization capabilities of LLMs.” 

This statement is unclear. The PDA framework is specific to Lean4 and the technique or evaluation doesn’t really convince me that the technique would enhance LLMs ability to autoformalize for any formal language. The claim about generalizability to other formal languages is not sufficiently supported by the current implementation and evaluation, which are narrowly focused on Lean4. The paper needs to provide a more detailed explanation of how the process-driven feedback mechanism can be adapted to other formal systems, considering the differences in syntax, semantics, and compiler feedback mechanisms across various formal languages. For instance, how would this framework apply to systems like Coq or Isabelle, which have different proof styles and compiler outputs?


- Line 176: “The real test set is constructed by collecting natural language math questions and answers from LI et al. (2024).” Can you give more information about the real test than this? What is the reason for generating this subset? Can you also give more information on the cited source. The description of the real test set is too brief. The paper should specify the nature of the questions, their difficulty level, and the source of the questions within the cited work. It is unclear why this specific subset was chosen and how it differs from the other test sets. More details are needed to assess the relevance and representativeness of this real test set for evaluating autoformalization capabilities.


- Line 194: “during informalization, the provided proof steps could potentially add informative context to the preceded formal theorem statement in the prompt, hence improving informalization quality, observed both in our human evaluation results (Table 6)” - How does results from Table 6 infer the observation made here? The link between the observation about improved informalization quality and the results in Table 6 is not clear. The paper should provide a more detailed explanation of how the data in Table 6 supports this claim. Specifically, which metrics or comparisons in Table 6 demonstrate the positive impact of proof steps on informalization quality? A more direct and explicit justification is needed.


- Line 197: “ in autoformalization, the existence of proof steps also enables us to examine autoformalization performance by assessing the validity of the formalized combination of theorem statements and proof using a compiler, increasing the difficulty and granularity of autoformalization evaluation.”
Is it not possible to use the Lean4 compiler with statement + empty proof to get the compiler feedback on the theorem statement? The paper does not adequately explain why the inclusion of proof steps is necessary for compiler-based evaluation. It is unclear why the Lean4 compiler cannot provide feedback on the theorem statement alone, without a proof. The paper needs to clarify the specific advantages of using statement-proof pairs for compiler feedback, compared to using statements alone.


- Line 201-208: It is still unclear to me what this part is inferring. One of the main contributions of the paper in comparison to prior works mentioned in Table 2, is that FormL4 consists of proofs and the primary usage is for process-driven feedback. Does this mean FormL4 dataset consists of incorrect proofs of theorems? Yet, these incorrect proofs are useful for the autoformalization task to provide better context? The role of proofs in the FormL4 dataset and the PDA framework is not well-defined. It is unclear whether the dataset contains incorrect proofs, and if so, how these incorrect proofs are useful for autoformalization. The paper needs to clarify the nature of the proofs in the dataset and their specific purpose in the autoformalization process. The explanation should clearly distinguish between correct and incorrect proofs, and their respective roles.


- Line 259: “The average success rate was 0.72, indicating relatively high-quality informalization performance.” How do I assess that this is high-quality? Relative to what? The claim that a 0.72 success rate indicates high-quality informalization is not well-supported. The paper needs to provide a clear benchmark or comparison to justify this claim. It should specify what constitutes high-quality performance in this context and provide a rationale for why 0.72 is considered high relative to other existing methods or datasets.

### Questions
Please see questions in the weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a new benchmark and evaluation framework for autoformalization in Lean 4 called FormL4. In order to improve autoformalization ability, the authors also introduce PDA, Process-Driven Autoformalization, which uses feedback from Lean 4's interpreter.

### Strengths
- Autoformalization is an important problem, and there is not yet a good benchmark in the literature measuring its success, so the problem this paper tackles is important and relevant
- Incorporating execution feedback during autoformalization is a new idea
- The method presented in the paper shows strong performance compared to off-the-shelf models.
- The benchmark is curated with a combination of automation and manual checking.

### Weaknesses
 - Because the dataset was constructed from LLM-based informalization, I am not convinced of the quality of the benchmark. I read Appendix F, and while the authors do run a human manual check, only a small number of samples seem to be checked. In addition, the human success rate found was only 72%, which does not seem sufficient when the samples are being used for a benchmark.
- The PDA framework uses compiler feedback as a signal for correctness, while the final evaluation is whether the generated code compiles. Code that compiles is not necessary correct, so the final metric could potentially be misleading and not be a good measure of true autoformalization ability.
- Mathlib theorems may require a lot of dependencies and external knowledge in order to understand. In addition, there are niche primitives in Mathlib that the model has little chance of understanding. Unless these are filtered out, this benchmark feels like it is testing knowledge of obscure Mathlib premises.
- There is a potential contamination issue. Because the "correct answers" in the dataset are directly copied from Mathlib, models trained on Mathlib will have an unfair advantage in this evaluation. This is a significant concern that could invalidate the benchmark results.
- The evaluation metric, while using compiler feedback on both statement and proof, still only achieves a 75% success rate when both compile, and 50% when the proof fails to compile. This is not high enough for a benchmark, and it is unclear how the evaluation handles multiple valid autoformalizations of the same statement. It is also likely that not all statements are compatible with all proofs, due to the way Lean handles rewrites and the different theorems available for different types (e.g. natural numbers vs integers).

### Questions
- How do you ensure that all the samples in the benchmark are correct and reliable?
- There could be many potential autoformalizations of an informal statement. How do you ensure that correct autoformalizations are marked as correct, and incorrect ones are not? Do you just use compilation? Is your method reliable, and do you have any estimations of the precision/recall of the resulting evaluation?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces two main contributions to improve autoformalization (converting natural language mathematics into formal languages) for Lean 4, a modern theorem prover:

1. FormL4: A comprehensive dataset containing 17k examples designed to evaluate autoformalization capabilities in Lean 4. Unlike existing datasets that only contain theorem statements, FormL4 includes both statements and their corresponding proofs in both natural and formal languages. The dataset features three test sets: random, basic (focusing on fundamental concepts), and real (derived from real-world math problems).
2. Process-Driven Autoformalization (PDA): A novel framework that leverages detailed feedback from the Lean 4 compiler to enhance autoformalization. The framework consists of:
    - A Process-Supervised Verifier (PSV) trained using step-level compiler feedback
    - An iterative refinement strategy combining Rejective Sampling Fine-tuning (RFT) with a Verifier-Enhanced Autoformalizer (VEA)

Through extensive experiments, the authors aim to demonstrate that their PDA framework significantly outperforms existing approaches, with the combined RFT+VEA model showing the best performance across all test sets. The process-supervised training approach consistently outperforms outcome-supervised methods, and the authors do a human evaluation to validate the effectiveness of their approach.

### Strengths
1. Originality
    - The core idea of using compiler feedback in a systematic way to improve autoformalization is valuable and is implemented in a novel way
    - The attempt to create a comprehensive dataset for Lean 4 that includes both formal and informal pairs of both statements and proofs addresses an important gap in the field
    - The process-driven approach to verification represents a new direction in autoformalization
2. Quality
    - The methodology for preventing formal terms from appearing in autoinformalized descriptions is well done and well documented (Appendix C)
    - The experimental setup includes multiple meaningful test sets (random, basic, and real-world)
    - The approach to compiler feedback integration is technically sound in concept
    - The code and data will be made public, supporting reproducibility
3. Clarity
    - The overall paper structure follows a logical progression
    - The technical writing at the sentence level is generally clear
    - The motivation and potential impact are well articulated
4. Significance:
    - The paper addresses important challenges in automating formal verification:
        - The problem of autoformalization for Lean 4 is significant and timely
        - Using compiler feedback for training could be valuable even beyond this specific application
        - The attempt to bridge informal and formal mathematics remains an important goal
        - This kind of approach could reduce the burden of formal verification

### Weaknesses
The strengths above are significantly undermined by:

- Systematic and apparently hyperbolic misrepresentation of dataset quality
- The lack of proper baselines and controls
- Missing adequate qualitative analysis of failure modes
- Serious methodological flaws in evaluation
- Potentially misleading reporting practices

Significant concerns in detail:

- L166—167: Is any effort made to ensure that we don’t have pairs of lemmas that are essentially the same (for example, one proving `x=y` and another proving `y=x`) which end up on different sides of the train/test split?
- The paper seems to systematically obfuscate the quality of the FormL4 dataset.  The examples I found are:
    - L201—203 “It is important to note that translating proof steps is much more challenging than translating statements and that FormL4 does not aim at ensuring strict semantic alignment between formal and natural-language proof in our informalized output.” If the dataset does not guarantee a match between the formal and natural-language proofs, this caveat should be made much earlier in the paper.  This is especially the case given how much emphasis is placed on how FormL4 is “rigorously quality-checked manually” (L47—48)
    - L205—208: “the quality of FormL4 and our evaluation framework does not pertain to whether the natural-language proof perfectly corresponds to the formal proof.”  This sentence does not make sense.  While the evaluation framework is based on *usefulness* of the natural-language proof to generating the formal proof, and the soundness of the evaluation is not compromised in cases where the natural-language proof does not correspond to the formal proof (and would not be compromised even if the natural-language proof were nonsense), the semantic correspondence is certainly relevant to the *quality* of the dataset.
    - L213—215: “${}^5$ In practice, we observe that it is usually infeasible to perfectly translate a set of formal proofs to a natural language. This is because formal proofs are often expressed in pre-defined lemmas or environments that are exclusively constructed in the Lean 4 language, and there are no existing corresponding concepts in natural language that a non-expert in Lean 4 could easily understand.”  The first sentence here is misleading, and the second sentence seems bogus.  On line 202 you say that “strict semantic alignment” is not ensured, while here you say that “perfect[] transl[ation]” is infeasible.  Almost all tactics have a relatively-easy-to-understand description in natural language that, while perhaps imperfect, is strictly semantically aligned.  For example, you might transcribe an `auto`-like tactic by saying “This follows by combining facts x, y, and z in some order”, where `x` , `y`, and `z` are the lemmas found by `auto`.  Some steps might not be worth translating (for example, `clear h` , translated as “from this point forward, we will not make use of the fact that …”, might be worthless to include).  Moreover, even if tactics may be hard to describe, the proof objects generated by the tactics could certainly be translated with near perfection.
        
        Ultimately, the informalization should be permitted to elide details, but not to make incorrect steps; otherwise, you should drop the language that the entire dataset is of impeccable quality and restrict such claims to the alignment of statements in the dataset, while merely saying that the dataset includes potentially incorrect formal-informal proof pairs.
        
    - L256—257: “extensive manual verification” is used to mean “≈70% accuracy looking at ≈ 3% of the data”.  For a work involving formal verification to use “verification” to mean “at least ≈ 2% correct” is at least skirting the boundary of the code of ethics (specifically the “Uphold High Standards of Scientific Excellence” and "Be Honest, Trustworthy and Transparent” sections), if not outright violating it.
    - Table 14 is damning: getting 0.65% on MATH and 8.16% on GSM8K even with a fine-tuned Mistral (Full) model suggests that that high results on FormL4 are a result of either overfitting or of FormL4 not spanning a large enough difficulty range.  This should not be buried in Appendix N.
    - L1566—L1569: Where is the line for the final **baseline** model in Table 14?  What are its performance results?
- L245—247: What about the 20% of samples where Gemini failed?
- The evaluation (cf Table 4) does not measure the right baselines and fails to establish an absence of data contamination.  A proper baseline would involve comparison with an autoformalizer trained on randomized mislabeled data from FormL4 (pairs of informal-formal that are unrelated), as well as, ideally, a comparison with the closed source models that provide fine-tuning APIs when fine-tuned to do next token prediction on the FormL4 pairs (both randomized and correctly labeled).  (Another possibility for large models is putting a couple dozen randomly chosen examples in context.). Correspondingly, L423, “effectiveness of our dataset” might just be homogeneity between the train and test split.
- Qualitative evaluation of failure modes is inadequate:
    - L1284—L1289: “The incompatibility of certain theorem statements for informalization due to their topics or settings.”  What does this mean?  What are examples?  Please elaborate on this more in the text.
    - L1284—L1289: “Individual subjectivity in determining the condition constraints that need to be specified in natural language” Does this mean that most human-checked informalizations were merely incomplete rather than incorrect?  Can you include numbers for completeness of informalization separately for correctness / lack of error?
    - No examples of challenging cases or failure modes for formalization

### Questions
Questions:

- Figure 1 suggests that the PSV only includes information on which statement failed, not utilizing the error message from the proof assistant.  Is this right?
- L245—246: What does “success” mean in “informalization success”?
- L418-419: What are RFT and VEA?  How do they work?  This should be explained, not just referenced
- L512-515 “Those whose proof validity is true achieve significantly better autoformalization performance.”. I am very confused by this paragraph.  What is the difference between “proof validity” (whether the sample passes the Lean 4 compiler”) and “autoformalization performance” (whether or not the sample generated by the autoformalizer was a valid proof?)?  Is the difference that the latter also includes human evaluation of whether the formalized proof is faithful to the informal proof sketch?  Or is it only about faithfulness to the informal proof sketch and does not include proof validity?

Comments: 

- It might be better to use “verifier model” instead of “verifier” to better disambiguate between the Lean compiler and the PSV model.  I was confused, for example, at L361—362 “mitigating the potential for bias arising from isolated interactions between the autoformalizer and the verifier” before realizing that “the verifier” meant the PSV model.
- Table 4 and especially the discussion of synergistic benefits is lacking a test of statistical significance.
- L504: “in 12” what is 12?
- The end of section 5 could do with some rewording.  “Factorial Design” has nothing to do with the factorial function, “investigate whether the following variable changes will impact model […] performances” (L495—496) makes it sound like you're doing interventions rather than factor analysis, it's not clear how “Test Set Categories” is varied when doing factor analysis, and it should have a consistent name rather than changing to “Dataset Split” on L523.
- Section 6 needs significant rewording; I include minor comments below, but most egregiously, the second sentence (describing FormL4’s focus) seems to be confusing the dataset with the PDA method.
- L418—419: RFT and VEA should be explained, not just referenced

Minor comments:

- L141: Tense mismatch in “Existing datasets […] aims to create”
- L176—177: “LI et al.” seems miscapitalized?
- L190—191: “Statemen” is missing a “t” at the end
- L194—195: “preceded” ⇒ “preceding”
- L195—196: “[…] informalization quality, observed both […]” this sentence is run-on, consider splitting it at the “,”
- L326: the equation should not have a `[ht]` figure specifier.
- L491: “falls short of even empowered” incorrect grammar
- L493: “syntactically true” ⇒ “semantically valid” or “semantically meaningful”.  Unlike Python or C, a theorem statement in Lean that compiles is more than just syntactically valid.
- L519—520: “than due to their” is missing a word
- L533 “drive” ⇒ “driven”
- L534—536: incorrect use of comma to join two clauses with different subjects in “Unlike the existing dataset focuses, FormL4 focuses on tapping”; “focuses” is used as a noun in the first clause but a verb in the second clause, and hence the sentence is comparing the focuses of existing datasets to the dataset FormL4.
- L536 “statement” ⇒ “statements”
- L537 “Lean 4 compilers” ⇒ “the Lean 4 compiler”
- L539: you could include Agda as well.  Unlike the other proof assistants, proof terms are generally given directly and in full rather than using tactics.
- L1005—1008: You’re underselling FormL4 by describing it just as a way to keep up with changes in Lean.  Either that, or you’re drastically overselling it in the main body.
- L1011 “Lean 4’s syntax” should maybe be “Lean 4’s tactics”?  Not sure.
- L1073—L1074: you used `'` instead of ``` to start a quotation (twice)
- L1101—1102, L1110-1111: Does the prompt actually inconsistently capitalize “Lean”?
- L1203—1204: “their proof” ⇒ “their proofs”
- Section E.1: It is not clear what text is verbatim from your prompting and what text is descriptive for readers of the paper.  Presumably “you” in E.1.2 does not refer to the reader.
- L1310—1311, L1470—1471 you use `'` instead of ``` to start a quotation
- L1427—1428: Perhaps you should say “Lean 4’s compilation times are a bottleneck” instead of claiming that “there is significant room for improvement”, unless you know enough about proof assistant performance engineering to know that the performance improvement times you’re claiming are, in fact, possible.
- L1439—1440: Probably you want `\textsc{FormL}4` instead of `FORML 4`
- L1507: check capitalization of “Minif2f”
- L1690: you should get rid of the negative vspace, the text is overlapping the table
- You should make sure you're consistent (and correct) about using “Lean 4” vs “Lean4” (L1651, L217, L219, L492, L498, etc)
- If you want to, you can get small caps in the pdf bookmarks ToC by replacing the section heading (L1512) of `Analysis for Training and Test Data in FormL4` with `Analysis for Training and Test Data in \texorpdfstring{\textsc{FormL}4}{FᴏʀᴍL4}`  (and similarly with Appendix P.3)

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces a novel approach to autoformalization—the automatic translation of mathematical text into formal language—by creating a new dataset and framework specifically for Lean 4. The dataset, FORML4, includes both formal and natural language versions of mathematical statements and proofs, enabling a comprehensive evaluation of large language models (LLMs) in autoformalization tasks for Lean 4. The authors also propose the Process-Driven Autoformalization (PDA) framework, which iteratively improves model performance through Lean 4 compiler feedback. By incorporating a Process-Supervised Verifier (PSV) that identifies specific errors in the formalization process, the PDA framework enhances the semantic accuracy of formal translations. Experiments demonstrate that this approach boosts performance and data utilization efficiency. FORML4 and PDA together aim to push forward formal language generation quality and adaptability in mathematical reasoning tasks.

### Strengths
1. It creates a unique Lean 4 dataset (FORML4) with statements and proofs for comprehensive model evaluation.
2. The proposed approach PDA shows some improvements and also helped with the dataset.

### Weaknesses
I do not see significant weaknesses.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
3

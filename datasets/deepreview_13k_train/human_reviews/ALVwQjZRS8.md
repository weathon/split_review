# Coeditor: Leveraging Repo-level Diffs for Code Auto-editing

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Developers often dedicate significant time to maintaining and refactoring existing code. However, most prior work on generative models for code focuses solely on creating new code, overlooking the distinctive needs of editing existing code. In this work, we explore a multi-round code auto-editing setting, aiming to predict edits to a code region based on recent changes within the same codebase. Our model, Coeditor, is a fine-tuned language model specifically designed for code editing tasks. We represent code changes using a line diff format and employ static analysis to form large customized model contexts, ensuring the availability of appropriate information for prediction. We collect a code editing dataset from the commit histories of 1650 open-source Python projects for training and evaluation. In a simplified single-round, single-edit task, Coeditor significantly outperforms GPT-3.5 and SOTA open-source code completion models (bringing exact-match accuracy from 34.7 up to 60.4), demonstrating the benefits of incorporating editing history for code completion. In a multi-round, multi-edit setting, we observe substantial gains by iteratively conditioning on additional user edits. We have open-sourced our code, data, and model weights to encourage future research and have released a VSCode extension powered by our model for interactive IDE usage.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents Coeditor, a fine-tuned language model that is designed for code editing tasks. The backbone of the Coeditor is the CodeT5 model, which the authors have finetuned on long context (2k->4k->8k) using block-sparse attention and capitalizing the relative positional encoding scheme of CodeT5 model. Coeditor is built based on two key ideas: (1) encode prior code edits using a line-based diff scheme and decode the edits using the masked span infilling objective; and (2) using lightweight static analysis to pull in relevant parts of the codebase (e.g., function signature). The paper proposed a dataset called PyCommits which is collected from 1650 open-source Python projects on Github. The paper compared Coeditor with code infilling models - InCoder, Starcoder, text-davinci-003 and showed that Coeditor outperforms them by a large margin. Codeditor is released with code, dataset, model checkpoint, and a VSCode extension.

### Strengths
- A good dataset (PyCommits) that will foster future research.
- The proposed method to train sequence-to-sequence language models for code editing is sound. Overall, the writing is good (though there are minor grammar issues and repeated words) and the paper is easy to read and follow.
- An IDE extension that researchers will be able to use and understand the effectiveness of the approach.

### Weaknesses
The primary issue of the paper is over claim when it compares with SOTA code infilling models. Statements such as "our method achieves 60.4% exact match accuracy using a 220M parameter model, whereas text-davinci-003—the best performing code infilling model we have compared, which has 175 billion parameters—achieves only 30.5%." is extremely misleading. Coeditor is a finetuned model that is made by specializing on the task at hand. On the other hand, the infill models are general purpose models. The paper didn't explain clearly how the generic infill models are prompted to solve the code editing tasks. Therefore, there is no way we can fairly compare the proposed approach with the baseline models compared in this work.



### Questions
- Why Coeditor is trained with a fixed batch size of 1? The Nvidia GPU used to train the model has 48GB memory which should be good to accommodate batch size > 1 with a 220M param model, right?
- Does the PyCommits dataset composed of Github projects that have permissive licenses?
- How the generic infill models are prompted to solve the code editing tasks? Is few-shot prompting used for the models? For example, [1] used demonstration augmented prompting for Codex model (when finetuning is not possible).
- Can we use instruction finetuned version of the code generation models for code editing task?
- Instead of a seq2seq model, can we use a decoder-only LM for the editing task?
- Is it possible to evaluate Coeditor on the PIE benchmark [1]?

[1] Learning Performance Improving Code Edits (https://pie4perf.com)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Coeditor, a novel model for auto-editing code based on the CodeT5 transformer model architecture. It is designed to predict edits to existing code, based on the related recent changes in the same codebase. The tool requires users to manually select the code region for editing. The paper introduces a new PYCOMMITS dataset, sourced from 1650 open-source Python projects, which is used for evaluation. The model outperforms existing tools in both single-edit and multi-round editing scenarios and includes a VSCode extension for practical use. The paper highlights the importance of integrating editing history in code completion and provides resources for future research in this domain.

### Strengths
* Introduce and open source the new research PyCommits dataset, source code, and VSCode extension. Which is an important contribution to future research in this domain.
* A step towards solving an important practical problem, and a potential to integrate in real-world developer tools

### Weaknesses
 * One notable weakness of the Coeditor model is its reliance on users to manually pinpoint the regions in the code that need editing (as pointed by the authors, too). This approach limits the model's potential for broader applications, such as automated refactoring, and places additional steps in the workflow that could be automated for enhanced efficiency and user experience.

* The evaluation section could be improved by incorporating a more diverse range of baselines. Currently, it predominantly features large language models (LLMs) tailored for coding tasks.

### Questions
It would strengthen the paper if you could include any specialized code editing models or tools to the evaluation, which could provide a more comprehensive comparative analysis. 

I would be curious to see how CodePlan + Coeditor perform on the PyCommits dataset (especially since the CodePlan paper partially features the results using the Coeditor model), although I realized that CodePlan was published after the ICLR submission deadline. Is it possible to add?

Another interesting baseline could be BluePencil model focusing on repetitive edits (see "On the fly synthesis of edit suggestions" by Miltner et. al) this is also available through IntelliCode Suggestions VS extension.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to shift the focus from learning code completion to learning edits instead and leveraging repository wide line-diff information to do so. They build on top of CodeT5 which they augment with sparse block attention to enable larger context sizes needed for the new task to produce Coeditor. Further, they create a summary "scratchpath" that summarises useful, out-of-file information, the summarisation being crutial to avoid large prompts. They derive an edit history from the git histories of Python projects and use the current edited files as context at prediction time. Further, they integrate into VSCode as an extension to demonstrate how such a tool can work in a developer workflow. Crucially, the novel setting is the human-in-the-loop, multi-round editing, where a human may provide feedback between rounds. Evaluating using Exact Match, they demonstrate better performance both in single- and multi-round editing settings, demonstrating the befit of shifting to modeling edits directly, thr ablation study further demonstrates the value of diffs.

### Strengths
- A perspective shift to modelling code edits.
- A smaller scale model that outperforms larger models on the code auto-completion task.
- VSCode Extension that can be used directly in a project.
- A historical edits dataset for Python

### Weaknesses
 - The edit granularity choice and dataset can introduce bias: developers often commit many intermediate commits that get squashed into a single commit before pushing and changes can get overwritten.
- While the delta/diff encoding is justified, the space feels under-explored.

After reading the separate discussion threads, I share the concern of the reviewer vqdF regarding the use of signatures and their impact on performance. I am unconvinced that the information cannot be exposed to baselines, for example, by borrowing methodology from Ahmed et al. [^1].

### Questions
With the move towards an extension, was using more granular edit events considered, what about navigation events or other similar side-channel information? Is the main concern the context size or are there other trade-offs that moved the authors closer to git diff, line-level information?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Language models effectively model text generation in a single context, but programs are often written by altering code
across many files and locations. This work proposes to fine-tune a language model with a dataset of code "diffs", consisting of a series of edits that together comprise a meaningful change. Specifically, it introduces a block-sparse attention mechanism that allows the model to attend to many related changes without at a fairly modest cost and introduces "signatures" of used variables and functions. The resulting model offers strong results at single-line and multi-line prediction given previous edits compared to language models that are unable to leverage such information.

### Strengths
Utilizing recent edits in a language model trained on code is a natural choice and this paper offers a reasonable implementation of this idea. Compared to other recent work with the same general goal, it is particularly strong in its definition of reference block and the corresponding sparse attention pattern. This allows it to scale to fairly long contexts, which yields a modest boost in performance (Tab. 5).

While the results come with some concerns (see below), the "replace" performance in particular is quite promising. The work is also quite well written. Overall, this paper presents a promising exploration of its domain.

### Weaknesses
The evaluation raises some concerns, in particular the comparison with the baseline models. This work introduces a few components; the key one is the notion of reference blocks that CodeT5 can attend to when responding to a query. The baseline models do not have access to these reference blocks since they are trained on regular token streams. This creates a few issues, some of which can be resolved with clarifications in the writing and others that might require further experiments. In no particular order:

- There can be many reference blocks, spanning up to 16.4K tokens, so the work uses a relatively short "Query" of up to 1,024 tokens. Other LMs, such as InCoder and StarCoder, all have much larger context sizes. It is not clear from the writing whether the other models were "allowed" to use their full context window, or were provided with the same limited section of context. If a completion took place halfway through an 8K token file, one would expect StarCoder, for instance, to do substantially better with the full file context than with a 1K token window.
- A seemingly unrelated form of "reference" comes from the "signatures" (section 3.2). This idea does not have anything to do with code editing itself, but rather with providing an LM access to the project-level context. This seems to be very impactful (Tab. 5). It looks like the baseline LMs were not provided with this information, which seems like an oversight. For one, there are reasonable ways to prompt pretrained language models with such information even if that wasn't present at pretraining time. For another, the performance of this component has little, if anything, to do with the stated goal of the work (leveraging diffs for edit prediction). The fact that it boosts performance so strongly makes the results much less interesting; it suggests that a large component of the performance does not come from the presence of diffs, but from a more banal form of information that related work has already explored. The paper should either include carefully calibrated experiments with baselines using the same information or exclude this from its main contributions in results such as Tab. 3.
- Relatedly, it is not clear why there is such a large performance gap between Tab. 5 and Tab 3. The former uses the validation set, so one might expect that the latter is based on test data. The text in 4.3 does mention that the model was only halfway trained here. But the gap between 42.1% and 60.4% is really very large. Is this not the same type of task as in Tab. 3? And how should we expect the gaps between ablations to scale to the numbers of Tab. 3? In particular, would the impact of the retrieval blocks (criticized above) be proportional or even disproportionally larger?
- The lack of a comparison between models in Sec. 4.2/Tab. 4 is also somewhat surprising and concerning. Please endeavour to replicate these numbers with at least one strong baseline, e.g. StarCoder.

On a minor note, it was quite surprising to see it mentioned that the model was trained with a batch size of 1 (P7). Was gradient accumulation considered for increasing the batch size? That might improve performance.

Minor issues:
- P5: "making the model is" -> remove "is"
- P6: "statictics" -> "statistics"

### Questions
Based on the issues noted above:
- Were the baseline LMs evaluated with a 1K context, same as Coeditor, or with their maximum number of tokens (when possible)?
- Was signature information only used in Coeditor? If so, is this intended to be a core part of the contribution? Please provide ablations with other models using this information, and with Coeditor fully trained without this information in any case.
- How do the baseline models perform in the multi-round setting?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

# SWE-bench Multimodal: Do Autonomous Programming Systems Generalize to New Software Domains?

- Decision: Accept
- Scores: 6, 3, 6, 5

## Abstract
Autonomous systems for software engineering are now capable of fixing bugs and developing features. These systems are commonly evaluated on SWE-bench (Jimenez et al., 2024a), which assesses their ability to solve software issues from GitHub repositories. However, SWE-bench uses only Python repositories, with problem statements presented predominantly as text and lacking visual elements such as images. This limited coverage motivates our inquiry into how existing systems might perform on unrepresented software engineering domains
(e.g., front-end, game development, DevOps), which use different programming languages and paradigms. Therefore, we propose SWE-bench Multimodal (SWE-bench M), to evaluate systems on their ability to fix bugs in visual, user-facing JavaScript software. SWE-bench M features 617 task instances collected from 17 JavaScript libraries used for web interface design, diagramming, data visualization, syntax highlighting, and interactive mapping. Each SWE-bench M task instance contains at least one image in its problem statement or unit tests. Our analysis finds that top-performing SWE-bench systems struggle with SWE-bench M, revealing limitations in visual problem-solving and cross-language generalization. Lastly, we show that SWE-agent’s flexible language-agnostic features enable it to substantially outperform alternatives on SWE-bench M, resolving 12% of task
instances compared to 6% for the next best system.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces SWE-Bench MultiModal, an extended version of SWE-Bench, which addresses two limitations of the original version: (1) its focus solely on the Python programming language, and (2) its reliance on a single textual modality. The proposed benchmark overcomes these shortcomings by incorporating JavaScript as the primary programming language and adding images that reflect the issues being addressed, in order to assess the capability of language models (LMs) in generating multimodal patches. Additionally, the authors test the performance of existing LMs after adapting this benchmark to three systems: SWE-agent, Agentless, and RAG. Experimental results demonstrate that this benchmark remains a challenging one.

### Strengths
Overall, this work is commendable, and I believe the following points are particularly praiseworthy:

1. The introduction of multimodal autonomous systems for software engineering is a forward-thinking direction. By introducing this benchmark, the authors contribute to the community's understanding and research in this emerging field.
2. The experimental comparison of existing models is thorough, yet the primary aim is to highlight that this is a challenging and unsolved problem.
3. Significant contributions have been made in data collection and system adaptation, providing a solid foundation for guiding future research in this field.

### Weaknesses
However, from my perspective, I believe the paper could be improved in the following areas:

1. The authors claim that SWE-Bench only uses Python, limiting the ability to assess the generalization performance of language models, and use this as the motivation for proposing SWE-Bench MultiModal. However, this argument seems unconvincing. Although SWE-Bench M introduces JavaScript (and potentially other languages like HTML in the repository), a truly "generalizable" benchmark should encompass multiple programming languages, not just extend the original benchmark with a new one. The inclusion of JavaScript, while a step, does not sufficiently address the need for a broad, multi-language evaluation suite. A more compelling approach would involve a benchmark that includes a diverse set of languages, such as Java, C++, or Go, to truly test the generalization capabilities of language models across different programming paradigms and syntax.

2. Despite the extensive engineering adaptations made in this work, the benchmark seems somewhat lacking in innovation compared to SWE-Bench. SWE-Bench was created from scratch (0 -> 1), whereas SWE-Bench M is an extension (1 -> 1.5, maybe). The core contribution of SWE-Bench was the novel idea of using real-world GitHub issues as a benchmark for software engineering tasks. While SWE-Bench M builds upon this, it primarily adds a new modality and language, which, while valuable, does not represent the same level of conceptual innovation as the original SWE-Bench. The incremental nature of this extension raises questions about the overall impact and novelty of the work.

3. Multimodal software engineering is a highly attractive topic, but it seems unlikely that, in the foreseeable future, we will be able to solve it comprehensively in both practical applications and research. As a benchmark, simply increasing the difficulty of the tasks does not seem like a sustainable or effective direction. The current approach of adding visual elements and a new language might lead to a benchmark that is too challenging for current models, without providing clear insights into the specific limitations of these models. A more effective approach might involve a more nuanced benchmark design that allows for incremental progress and provides more granular feedback on model performance.

### Questions
1. I performed a preliminary review of the benchmark provided by the authors and noticed that a significant number of patches and test patches are empty. Does this suggest potential concerns regarding the quality of the benchmark?

2. I have questions about how the benchmark is evaluated. For example, how is the effectiveness of the generated patches in fixing new front-end pages assessed? The authors mentioned pixel-level visual testing, is this pixel-level comparison reasonable?

3. The authors should consider providing a complete repair process and examples to demonstrate how the system performs on the benchmark. This would offer a clearer understanding of how the system operates in practice.

4. The authors should consider showcasing several successful and failed cases to demonstrate that the successful cases across all models are not merely fixes for very simple problems. Additionally, it would be valuable to provide insights into the reasons behind the repair failures. This would help clarify the challenges and limitations of the current approach, offering a more comprehensive understanding of the model's capabilities and shortcomings.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces SWE-bench Multimodal (SWE-bench M), a novel benchmark designed to evaluate coding agents' ability to handle real-world software engineering tasks involving visual elements. The benchmark comprises 619 task instances collected from 17 JavaScript repositories, focusing on user-facing applications such as UI design, data visualization, and interactive mapping. Through rigorous analysis, the authors demonstrate that 83.5% of these tasks require images for proper resolution, highlighting the crucial role of visual elements in software development. The study reveals significant challenges in generalizing existing software engineering systems to handle both JavaScript and multimodal contexts, with even the best-performing systems achieving only a 12.2% success rate. The paper makes several key contributions: it provides comprehensive analysis of visual content in software development issues, introduces new evaluation methodologies for assessing visual reasoning capabilities, and reveals important insights about the limitations of current systems designed primarily for Python codebases. The authors also demonstrate that more flexible, interaction-based approaches perform better than rigid, pipeline-based systems when handling multimodal tasks, suggesting important directions for future development of software engineering systems.

### Strengths
This work exhibits rigorous data collection and validation processes, including comprehensive human validation of task instances, careful consideration of image necessity, and thorough experimental design with detailed ablation studies. The work addresses a significant gap in existing benchmarks by incorporating multimodality and tackling real-world challenges in software development. The dataset shows a diverse range of visual content types, and well-documented collection processes with careful consideration of licensing and reproducibility.

### Weaknesses
The paper has several areas requiring improvement, primarily in its framing and presentation. A significant issue is that the paper sometimes misframes its contribution by emphasizing Python-centric limitations of existing benchmarks, when its true novelty lies in targeting front-end development's inherent multimodality. The motivation for choosing JavaScript repositories should be more prominently centered on JavaScript's dominant role in front-end development and its natural incorporation of visual elements, rather than being positioned as addressing a gap in language coverage.

In addition, the evaluation methodology raises significant concerns about fairness and thoroughness in baseline adaptations. A major weakness is the oversimplified approach of merely swapping Python AST parsers with JavaScript parsers when adapting existing systems like Agentless and Moatless Tools. This superficial adaptation strategy leads to potentially premature conclusions about these systems' inability to generalize to multimodal tasks. The paper lacks a convincing demonstration that sufficient engineering effort was invested in properly adapting these baselines for multimodal scenarios.

The authors should have:
- Made a more rigorous attempt to adapt these systems for multimodal input handling, beyond just language parsing
- Documented failed adaptation attempts in detail to substantiate claims about generalization difficulties
- Explored architectural modifications that could enable these systems to better handle visual elements
- Referenced and learned from existing frameworks like HyperAgent[1] that successfully handle multiple programming languages and SE tasks

Without demonstrating that serious engineering efforts were made to strengthen these baselines, the paper's conclusions about the systems' generalization capabilities are not well-supported. The low performance of adapted baselines (3.9% for Agentless vs 11.5% for SWE-agent) might reflect inadequate adaptation efforts rather than inherent limitations of these approaches. A more compelling evaluation would require investing significant engineering effort to properly adapt these systems for multimodal tasks, even if this requires substantial work. This investment is necessary to make meaningful claims about generalization capabilities and to truly understand the challenges of adapting existing systems for multimodal software engineering tasks.

Finally, Table 1's comparison between SWE-bench M and other repository-level coding benchmarks is incomplete, notably missing comparisons with important related works such as DevEval[2], CrossCodeEval[3], and RepoExec[4]

### Questions
1) Could you provide more details about the engineering efforts made to adapt existing systems (Agentless, Moatless) for multimodal tasks?
2) Have you considered expanding to other visually-rich domains beyond web development (e.g., game development, mobile apps)?
3) Do you plan to expand the benchmark to include other front-end frameworks or visual-heavy domains?
4) How do you envision SWE-bench M evolving as models become more capable at handling multimodal inputs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work creates a new benchmark SWE-Bench Multimodal which address some limitations of prior benchmarks in this field that mainly focus on evaluation on Python only repositories. SWE-bench M provides a benchmark suite in JavaScript with the input  being to include also visual elements. SWE-bench M contains more than 600 different tasks complete with test cases to measure functional correctness. The authors further modify some existing state of the art open-source techniques and found that many of them require python-specific designs that limit their ability on the new benchmark

### Strengths
- Creates an important benchmark for an important area of measuring repository level code generation especially when the input is multi-modal
- Extensive manual effort used to ensure the benchmark is useable as well as adopt and modify baseline techniques

### Weaknesses
Overall, this is an important and usable benchmark, below are some weakness that I would love to see the authors address

**More analysis on the difficulty of the dataset**
- As the current demonstrate that SWE-bench M seems to be more diffcult than SWE-bench and SWE-bench lite, I would suggest the authors take a deeper look into the types of problems in SWE-bench and the reason why it is more difficult
- While the authors mentioned the mulit-modality aspect and the requirement of images, is that the only factor?
- It seems from looking at table 5 (the tasks without requiring images according to human annotators), the problems still appears to be more difficult that original SWE-bench lite problems
- More analysis into what makes these problem difficult would be beneficial to the research community 

**Improvements to Testing**
- Given the state of software development is test driven, I would like to see the authors make some effort in improving the test quality.
- As mentioned in text, the authors already filter out some "flaky" tests which are a good sign, however looking at the number of tests in Figure 5 and Table 9 in Appendix it seems the number of Fail to Pass tests are still limited.
- It would be great if the authors can apply some test augmentation or manually apply (while this might require tons of manual effort, it woud definitely improve the robustness of the benchmark) 

**More metrics than just pass or fail**
- One issue with repository level benchmarks (including SWE-bench) is that the metric used seems to be always whether the issue was resolved or not.
- For real-world software development, there are many steps to solving the problem from being able to identify the root cause, localize the code elements, writing tests that can reproduce the errors, and then finally applying the patch
- I believe that more intermediate metrics that can be used to gain more information from the results should be designed and applied. 
- This would aid in the design of new approaches as well as provide more analysis options espeically given the large cost of evaluation on repository level benchmarks like SWE-bench M

### Questions
- Given the low amount of changes required to go from SWE-agent to SWE-agent JS and SWE-agent M, I am curious if the authors have tried applying SWE-agent JS or SWE-agent M on the original SWE-bench tasks? if so what would be the performance?
- How are the human annotators chosen? the paper only mentions the number of annotators (3) in the Appendix, but no further details are provided

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the SWE-bench Multimodal (SWE-bench M), an extension of the SWE-bench benchmark for evaluating the performance of autonomous software engineering systems on their ability to fix bugs in visual, user-facing JavaScript projects. The dataset includes 619 task instances from 17 repositories, incorporating visual elements like screenshots, diagrams, and other assets to reflect real-world programming challenges more accurately. The authors also assess existing models developed for SWE-Bench on SWE-bench M, highlighting the limitations of current state-of-the-art approaches in handling visual information and cross-language generalization.

### Strengths
+ a new dataset for evaluating LLM-based issues resolving models
+ limitations of existing approaches on the new data were discussed

### Weaknesses
 - criteria for project and issue selections are unclear
- generalizability of the JS-based multimodel issues is limited
- there already exists a rich research body on multimodal bugs/issues---mobile bugs/issues
- the adaptions for existing models are mainly on the language level, it's unclear how to handle images/videos
- the comparison between these approaches on multimodal issues and text issues is missing
- how important the visual data (images/videos) in the process of bug fixing is unknown

### Questions
1. This work extended SWE-Bench, while major challenges encountered during data collection may be similar to those in SWE-Bench. Could authors clarify what unique challenges were faced in data collection for this work compared to SWE-Bench?

2. There is an established research body on reproducing/fixing multimodal bugs in mobile apps, while this work focuses on JavaScript bugs. What is the motivation behind focusing specifically on JavaScript-based multimodal bugs, given there already exist mobile app bug datasets?

3. The data collection process inlcudes five steps, but the criteria for each step are unclear. For example, in step 1, the authors selected 17 repositories. What was the project sample size after applying the filters (e.g., 5,000 or more stars and 500 or more pull requests)? Step 5 includes human validation, how many authors involved? How to solve the conflict during the process?

4. "From 135k PRs, this new filtering criteria yields 1,478 candidate task instances." Does this indicate that the identified bugs are relatively uncommon or corner cases? How important is the importance of these collected multimodal bugs compared to text-only bugs?

5. Do the baseline models perform significantly differently on multimodal issues than text-only issues within these JavaScript projects?

6. The impact of visual data (images/videos) on the bug-fixing process is unclear; the performance decline without images/videos is around 3%. Does this imply that images/videos are unimportant for these tasks?

### Soundness
2

### Presentation
3

### Contribution
2

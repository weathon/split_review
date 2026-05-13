# ScreenWriter: Automatic Screenplay Generation and Movie Summarisation

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
The  proliferation of creative video  content has driven demand for textual descriptions or summaries that allow users to recall key plot points or get an overview without watching. The volume of movie content and speed of turnover motivates automatic summarisation, which is nevertheless challenging, requiring identifying character intentions and very long-range temporal dependencies. The few existing methods attempting this task rely heavily on textual screenplays as input, greatly limiting their applicability. In this work, we 
propose the task of automatic screenplay generation, and a method, ScreenWriter, that operates only on video and produces output which includes dialogue, speaker names, scene breaks, and visual descriptions. ScreenWriter introduces a novel algorithm to segment the  video into scenes based on the sequence of visual vectors, and a novel method for the challenging problem of determining character names, based on a database of actors' faces. We further demonstrate how these automatic screenplays can be used to generate plot synopses with a hierarchical summarisation method based on scene breaks. 
We test the quality of the final summaries on the recent MovieSum dataset,  which we augment with videos, and show that they are superior to a number of comparison models which assume access to goldstandard screenplays.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a complete system to take an entire movie with associated audio track and automatically creates a textual summary of the movie. For the system a set of mostly existing methods are integrated into a full solution. The two elements that are (according to the authors) new are the scene segmentation and character identification method, for the text generation a standard LLM is employed.

### Strengths
- a complete system addressing all modalities
- well written, easy to read
- potential for interesting applications

### Weaknesses
 - The tasks for the given "new" algorithms go back to the 90's of the previous century. Yet the methods are compared to non-algorithmic baselines like just doing random or uniform assignment. For example the Scene Transition Graph by IBM from 1997 (https://www.spiedigitallibrary.org/conference-proceedings-of-spie/3312/1/Classification-simplification-and-dynamic-visualization-of-scene-transition-graphs-for/10.1117/12.298470.short) and the NameIT system by Satoh (Name-it: Naming and detecting faces in news videos
S Satoh, Y Nakamura, T Kanade - Ieee Multimedia, 1999). Both have a multitude of citations so hence many follow-up systems. The authors should do a thorough review of the field and compare their methods to the best performing ones.
- Overall the system seems very much to be extensions of the work of Lapata which are the only ones mentioned in long-form summarization. Authors should do a far more in-depth analysis of the field. I googled "automatic summarization of complete movies" and already got a number of papers which are related. Authors should indicate how their method is different from those. 
- This is not a typical ICLR paper where the main contribution of the paper is on the algorithmic side. As indicated above the contribution in terms of algorithms is limited so the main novelty is the integration of all of these into one system. Other venues like ACM Multimedia, SIGIR, or a similar conference are far more suited for that topic, so my suggestion would be to improve the work and submit the work there.

### Questions
Questions:
- What makes the two algorithms innovative if there is already so much out there?

- The objective: the movie application is exactly where these kind of techniques for automated objective textual summarization seem less interesting as you can find a movie summary for every movie at the IMDB website and if not, likely the actors can also not be found there. Personalized summaries of movies are in my opinion more interesting (although even more difficult to evaluate, you should probably work with real users for that). Another issue with the objective is that a typical summary should not contain any spoilers where the current system doesn't take that into account. 

Remarks:

Scoping:  The paper says that summarization is usually done from the text perspective but that is maybe true for the NLP community but in Computer Vision there is (and has been from the 90's) a lot of work on visual video summarization. Many of those are referring to the datasets you are also mentioning (like MovieSum). So the authors should remove this claim (or substantiate it with evidence based on citations) and consider the computer vision driven video summarization literature and make more clear how the current work is different. 

Ref [Abhimanyu Dubey] is not proper. The CLIP website actually gives you a proper way to refer to it.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a new problem of automatically generating the screenplay of a full-length movie (which is typically of at least 90 minutes length) utilizing only the video and audio information. The primary motivation is for movie summarization (as inferred from the title of the paper). This assumes that the actual original screenplay, based on which the movie had been originally shot, is unavailable. The method has four main components - text transcript generation from audio which essentially performs speaker diarization, video scene detection, identification of the names of the characters in the movie and associating them with the transcript using the face images, and finally screenplay generation using caption generation of three key-frames per scene. The contributions are (a) the new task (b) scene boundary detection algorithm (c) detection of character names. Evaluation results are provided for scene detection, character name assignment and movie summarization in text using the generated screenplay.

### Strengths
The strengths of this paper are:

(1) The authors propose a new task for movie content processing i.e. generating the screenplay of the movie using only the video and audio content of that movie.

(2) The authors have proposed a solution framework, as captured in Figure 1, which is both plausible and also provides scope for improvement for follow-up work.

(3) The quality of the summary generated, as shown in the example, is very good even when compared to the gold standard.

### Weaknesses
 (1) The motivation of the paper is somewhat weak and can hope fully be strengthened. It is assumed that the screenplay of a movie is not available. Given that screenplays exist for all movie created (including the nascent attempts at creating movies using diffusion models), why not just purchase them? They are apparently available at www.scriptly.com (for example the screenplay for the movie Oppenheimer is available for $24.95 on that site), it does not seem worthwhile to work on this problem. Other than just taking it up as an intellectual challenge. It would be good to strengthen the motivation. A possible way to strengthen it is by thinking of situations where the screenplay might not be available. Or if there is a divergence between the original screenplay and the actual movie which could be captured via the generated screenplay.

(2) In general, it appears that the authors are not familiar with the literature in the multimedia content processing and computer vision areas. Scene boundary detection has been researched there for decades and while the proposed method appears to be novel, a proper literature survey needs to be done. Even NetFlix and Amazon Prime have published methods:

https://netflixtechblog.com/detecting-scene-changes-in-audiovisual-content-77a61d3eaad6
https://www.amazon.science/blog/automatically-identifying-scene-boundaries-in-movies-and-tv-shows

A comparison with the state of the art methods such as the above ones and also in the literature, will help establish the novelty as well as the superiority of the proposed approach.

(3) The name assignment method is simple and effective. However, it appears that there could be misses and also incorrect assignments. The frequency of its occurrence seems to be roughly 34% from Table 2. It is not clear what is the impact of these errors on the quality of the screenplay generation and also on the summarization?

(4) While the paper provides evaluation results for the summarization task, no evaluation is provided for the main work of the paper which is the screenplay generation. Why is there no quality evaluation of the screenplay generated by the proposed method? Only the indirect measure via the quality of summary generated is provided. It would strengthen the paper if an evaluation is done by comparing the generated screenplay with the original screenplay, perhaps using some of the text processing metrics used for the summary comparisons.

### Questions
(1) Please discuss the quality of the screenplay output of the method.
(2) What would be the quality of the summary generated by the name-only prompt of the current leaders of the ChatBot Arena (say ChatGPT-4o, Gemini 1.5 and Claude 3.5)? if it is substantially better than the proposed method, then the case for the proposed research will be weakened.
(3) In Table 3, the name-only prompt results are actually quite impressive. It is not clear why the quality degrades when more information is provided i.e. full script and whisperx script. That appears to be a bit counter-intuitive.

### Soundness
3

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
This paper presents a system for generating automatic screenplays and summaries from movies. The system is a combination of several well-established techniques, including keyframe extraction, speaker diarization, face recognition, and scene segmentation.

After carefully reviewing the authors' responses, I believe this research would be highly valuable if the authors shared their code with the community. I would be willing to change my rating to 'above threshold' if the authors decide to make their code open source.

### Strengths
- Good Application: This system has many potential everyday applications. 
- Scene Detection: Introduces a novel, parameter-free scene boundary detection method based on the minimum description length principle.   
- Character Naming: Proposes a new algorithm for identifying and assigning character names based on a database of actors' faces.   
- Hierarchical Summarization: Employs a hierarchical approach for summarizing movies, first condensing individual scenes and then fusing them into a final synopsis.   
- Zero-Shot Learning: Utilizes zero-shot prompting for summarization, demonstrating the potential of leveraging large language models without task-specific fine-tuning.

### Weaknesses
Novelty: The system primarily combines existing techniques like keyframe extraction, speaker diarization, and face recognition into a single pipeline. While the integration of these techniques is non-trivial, it may be more convincing if the paper can clarify the contribution of each component and identify their novelty. 

More Comparison: The paper lacks a comparative analysis with current powerful LLMs, both publicly available models like GPT-4 and Gemini. In addition, it is not clear how the commercial system (Otter AI) is used in comparison. It will be crucial to dig deep to assess the  potential advantages and disadvantages of the proposed system.

### Questions
- It seems this paper only uses text and audio as input, and does not consider image and visual input. Is my understanding correct? [Updated: from author responses, this submission uses visual input]. 

- From the paper it is not clear what are the details of Otter AI. I am not sure whether the comparison is done by using the product, or reimplementing the paper published in 2023.

- Consider expanding the evaluation by including additional metrics, especially end2end user evaluation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces ScreenWriter, a framework that generates screenplays and movie summaries directly from video and audio without relying on text-based transcripts. Designed to address the growing demand for video summarization, ScreenWriter overcomes limitations of existing methods that require screenplay or transcript data by operating solely on video content.  The framework includes several modules: 1. Scene Detection algorithm 2. Character Name Assignment algorithm 3. Screenplay and Summary Generation.

### Strengths
1. The paper proposes a scene detection algorithm to divide long video sequences into chunks. It segments a sequence of visual feature vectors into scenes by minimizing a cost function based on the minimum description length principle, encoding each scene’s vectors relative to their mean, and using dynamic programming to efficiently find the optimal partition.

2. The paper proposes a character face assignment algorithm to associate specific character names with the screenplay, incorporating face similarity between a character bank and scene information.

### Weaknesses
1. Most components of the proposed framework are adopted from existing works, lacking academic and technological contributions. There is almost no insight provided on summarizing long-context videos using a “screenplay.”

2. The paper lacks an ablation study on the effect of different model sizes/types on the summarization results.

3. The screenplay generation process seems somewhat unnecessary. If the transcript is summarized and then processed by the summarizer alongside visual information in parallel, why is a screenplay still needed? The intermediate screenplay representation is not well-justified; it's unclear why the summarization process needs this intermediate step rather than directly processing the segmented transcript and visual data.

4. The baseline selection in the experiment lacks justification. For face assignment, randomly assigning or commonly assigned methods are not ideal choices. For scene detection, there is no comparison with classical tools like SceneDetection.

5. There are existing video summarization frameworks, such as MM-VID[1], MM-Narrator[2] and MM-ScreenPlayer[3], that show high similarity in their pipelines. A discussion of these works should be included.

6. Some typo:
    - 'sctructure' in line 67 should be 'structure'
    - 'movide' in line 317 should be 'movie'

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

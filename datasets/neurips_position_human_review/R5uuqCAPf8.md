# Stop DDoS Attacking the Research Community with AI-Generated Survey Papers

- Decision: Accept (Oral)
- Scores: 7, 4, 8

## Abstract
Survey papers are foundational to the scholarly progress of research communities, offering structured overviews that guide both novices and experts across disciplines. However, the recent surge of AI-generated surveys, especially enabled by large language models (LLMs), has transformed this traditionally labor-intensive genre into a low-effort, high-volume output. While such automation lowers entry barriers, it also introduces a critical threat: the phenomenon we term the "survey paper DDoS attack" to the research community. This refers to the unchecked proliferation of superficially comprehensive but often redundant, low-quality, or even hallucinated survey manuscripts, which floods preprint platforms, overwhelms researchers, and erodes trust in the scientific record. In this position paper, we argue that we must stop uploading massive amounts of AI-generated survey papers (i.e., survey paper DDoS attack) to the research community, by instituting strong norms for AI-assisted review writing. We call for restoring expert oversight and transparency in AI usage and, moreover, developing new infrastructures such as Dynamic Live Surveys, community-maintained, version-controlled repositories that blend automated updates with human curation. Through quantitative trend analysis, quality audits, and cultural impact discussion, we show that safeguarding the integrity of surveys is no longer optional but imperative to the research community.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
5

### Summary
This paper argues that the unchecked growth of AI-generated survey papers, often redundant, superficial, or hallucinated, is flooding preprint platforms and harming the quality, trust, and usability of academic literature. The authors term this trend a "survey paper DDoS attack." Through empirical evidence from arXiv (e.g., rising paper volume, increased AI-content scores, and abnormal submission patterns), the paper shows a post-ChatGPT surge in questionable survey output. It raises concerns about quality, ethics, and scholarly value. As a solution, the authors call for transparency in AI usage, stronger peer review norms, and propose a new model: "Dynamic Live Surveys," collaboratively maintained and version-controlled repositories integrating AI tools with expert oversight.

### Strengths
The paper takes a strong and timely stance on a rising issue with well-substantiated arguments. It combines empirical data with cultural analysis, presents a novel metaphor (“DDoS”), and proposes actionable recommendations and a forward-looking alternative (Dynamic Live Surveys). Its tone is measured, critical of misuse, but not anti-AI.

### Weaknesses
While well-argued, the paper could further explore how to reliably distinguish between responsible and irresponsible use of LLMs, especially given the detection limitations it mentions. The “Dynamic Live Surveys” proposal, though compelling, remains largely conceptual and may benefit from a more concrete feasibility discussion. Furthermore, it could engage more with how different disciplines outside CS have handled similar synthesis challenges.

### Questions
- How might Dynamic Live Surveys be governed in a decentralized yet quality-assured way? How do we real-time benchmark it in Production environment ?
- Is there a risk of overcorrecting and discouraging useful AI-assisted contributions? How can that balance be maintained?
- Could the proposed detection heuristics be integrated into arXiv moderation or conference review pipelines practically and automated ?

### Presentation
4

---

## Human Reviewer 2

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
This paper raises an important issue of AI-generated surveys as a DDOS attack on academia.

### Strengths
First off I think this is an interesting paper. 
What I like 
1. The idea of the living survey
2. The definition of abnormal authors
3. The potential detection metrics (section 3.2)

### Weaknesses
to what extent does the AI-generation score actually predict AI-generated content? The concern raised from two issues:

1. There have been some papers talking about LLM writing detection tool not being reliable https://direct.mit.edu/qss/article/doi/10.1162/qss_a_00368/128867/Where-there-s-a-will-there-s-a-way-ChatGPT-is-used and thus researchers have developed their own tools based on LLM-revising texts (ground truth 1), see https://www.cell.com/patterns/fulltext/s2666-3899(23)00130-7 and https://arxiv.org/abs/2404.01268 and a lot of others. I looked into the tool authors used and I found that https://huggingface.co/desklib the lab that developed this tool is not that reliable.

2. ChatGPT was released at the end of 2022 which arguably started all these "ddos attacks". If the argument holds true, then we should observe a huge increase in AI-generated surveys across multiple measures, a strong increase compared to 2022. OK i see this from the figure 1 mid panel which is nice, but for the left and right panels I don't see this trend which makes me further concern the reliability of the conclusion and reliablity of the measures (abmormal authors etc) -- they are nice measures and make sense intuitivly but not experimentally.

### Questions
How exactly are DDoS attacks linked to survey papers? it is less clear -- my feeling is just that we have too many AI generated survey papers, ok i buy it -- but authors claimed that "Instead of helping the research community to digest a field, it starts to **feel like** a DDoS attack, flooding the field with more content than anyone can reasonably read or use." I don't think it is a substantive link, and framing this to a DDOS attack seems to be overselling

### Presentation
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This position paper argues that the research community is currently being flooded by AI-generated survey papers, since LLMs such as ChatGPT came to mainstream use. The authors refer to this as "DDoS attack on survey papers", comparing to distributed denial-of-service attacks, when a large volume of mediocre quality inputs crowds out meaningful work. Through empirical analysis of arXiv data specific to CS community including citation patterns and author behaviors the paper show that there is a post-2022 spike in AI-generated surveys, many of which lacks quality. The paper also critiques the motivations behind such papers and discusses their impact on trust we have as a community on research, associated stress on reviewers and overall culture. It proposes some solutions including stricter reviewing standards, AI-detection protocols and also the need for Dynamic Live Surveys as an alternative to current standard reviewing methods.

### Strengths
The issue of spike in AI-generated review papers has been lunch-table conversation in academia in the past few years. This paper is timely and raises systematically a pressing issue we have in the research community and puts in the context of a position paper. The topic is therefore widely relatable and of course somewhat controversial. The authors argue their opinion clearly with empirical evidence. The paper also does well to anticipate counterarguments and handle them reasonably.

### Weaknesses
The analysis of the paper is based on simple heuristics such as counting papers with certain keywords, checking for overlapping citations and using AI-content detectors. While this may be reasonable for a position paper, the paper claims may be strengthened using better methods:

- Compared the citation overlap against a random baseline to see what counts as abnormally high
- Use similarity scores or similar to measure how repetitive the content actually is
- Also what about false positives such as single authors who wrote multiple high-quality surveys since they are experts in the field, this is a possibility as well.  

Additionally, the paper does not appear to address alternative methods to approach the problem: 
- Should we be encouraging multimodal, code-linked or interactive alternatives instead? 
- For example, are "reviewed" presentations a better format overall long form text-heavy survey papers? 
- Should there be review papers at all?

### Questions
The proposal for Dynamic Live Surveys is interesting, but does not go into the deeper implementation challenges:
- For example, how will hallucinated content from LLMs be caught here?
- How will incentives and moderation be handled at scale? 
- Who oversees the taxonomic revisions?  What happens when there conflicting edits? 
- How can hallucinations or biased outputs be controlled for dynamic live surveys? 
- Are human reviewers re-verifying every update?

### Presentation
3

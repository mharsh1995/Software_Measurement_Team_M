# Software_Measurement_Team_M
Correlation between metrics of Various Projects
=======================
The aim of this project is to measure different projects using different metrics and to co-relate them.
Here we perform various different coverage tests for developing test cases so that entire code is covered and there are no parts of the code left uncovered. The coverage helps us to make better test suites that can detect the anomalies and code mutants injected in the main code. The various coverages used to for code coverage are: 
1. **Statement Coverage:** measurement procedure wherein the number of lines of code covered under certain circumstances is calculated based on the inputs from the users.
2. **Branch Coverage:** Branch coverage is a measurement to calculate the number of branches executed per user input.
3. **Mutation Score:** Mutation score is a testing practice wherein we check the accuracy or precision of the test cases.
4. **Cyclomatic Complexity:** Cyclomatic Complexity is the measure number of linearly independent paths that can be executed in a program.
5. **Metrics based Software Maintenance Effort Model:** A model for estimating adaptive software maintenance effort in person hours, the adaptive maintenance effort model (AMEffMo) 
6. **Software Defect Density:** Defect Density is the number of defects confirmed in software/module during a specific period of operation or development divided by the size of the software/module

#### Various Projects Used:
1. **Apache Commons Math** - [*project details*](https://commons.apache.org/proper/commons-math/) , [*source-code*](https://github.com/apache/commons-math) 
2. **Apache Commons Pool** - [*project details*](https://commons.apache.org/proper/commons-pool/) , [*source-code*](https://github.com/apache/commons-pool)
3. **Apache Commons FileUpload** - [*project details*](https://commons.apache.org/proper/commons-fileupload/) , [*source-code*](https://github.com/apache/commons-fileupload)
4. **Apache Commons IO** - [*project details*](https://commons.apache.org/proper/commons-io/) , [*source-code*](https://github.com/apache/commons-io)
5. **Apache Commons Collections4** - [*project details*](https://commons.apache.org/proper/commons-collections/) , [*source-code*](https://github.com/apache/commons-collections)

#### Directory layout
    .
    ├── Projects                           # Data Analysis and Data Collection for different metrics
    ├── DataAnalysisNoteBook               # Scripts for finding Correlations     
    ├── Project Source Code                # latest version of project
    ├── Docs                               # Documentation files (alternatively `doc`)
    └── README.md
#### Prerequisites and Installation Steps for EclEmma (JaCoCo)
1. Prerequisites : EclEmma requires Eclipse 3.8 or higher and Java 1.5 or higher. It has no dependencies on a particular operating system. Of course your Eclipse installation needs to contain the Java development tools (JDT) which is included in the default SDK installation.
2. Installation Steps: 
```
    Step 1. From your Eclipse menu select Help → Eclipse Marketplace.
    Step 2. Search for "EclEmma".
    Step 3. Hit Install for the entry "EclEmma Java Code Coverage".
    Step 4. Follow the steps in the installation wizard.
```
3. Verification : The installation was successful if you can see the coverage launcher in the toolbar of the Java perspective.

#### Configuration for PIT Testing
1. PIT requires Java 5 or above and either JUnit or TestNG to be on the classpath.
2. Add the plugin to build/plugins in your pom.xml
```
<plugin>
    <groupId>org.pitest</groupId>
    <artifactId>pitest-maven</artifactId>
    <version>LATEST</version>
    <configuration>
	<threads>
		24
	</threads>
	<targetClasses>
		<param>your.package.name.*</param>
	</targetClasses>
	<targetTests>
		<param>your.package.name.*</param>
	</targetTests>
	<timeoutFactor>
		0.25
	</timeoutFactor>
	<timeoutConstant>
		1000
	</timeoutConstant>
	<mutationUnitSize>
		5
	</mutationUnitSize>
	<exportLineCoverage>
		true
	</exportLineCoverage>
	<maxMutationsPerClass>
		3
	</maxMutationsPerClass>
	<testPlugin>
		junit
	</testPlugin>
	<withHistory>
		true
	</withHistory>
	<outputFormats>
		<outputFormat>CSV</outputFormat>
		<outputFormat>HTML</outputFormat>
	</outputFormats>
	</configuration>
 </plugin>
 ```
 3.  Mutation Coverage : It can be run directly from the commandline
 ```
 mvn org.pitest:pitest-maven:mutationCoverage
```
 4.  To speed-up repeated analysis of the same codebase : It can be run directly from the commandline
 ```
 mvn -DwithHistory org.pitest:pitest-maven:mutationCoverage
```
 

#### Installation and Configuration for CLOC
1. Depending your operating system, one of these installation methods may work for you:
```
  npm install -g cloc                    # https://www.npmjs.com/package/cloc
  sudo apt-get install cloc              # Debian, Ubuntu
  sudo yum install cloc                  # Red Hat, Fedora
  sudo pacman -S cloc                    # Arch
  sudo pkg install cloc                  # FreeBSD
  sudo port install cloc                 # Mac OS X with MacPorts
```  
2. To run cloc on Windows computers, one must first open up a command (aka DOS) window and invoke cloc.exe from the command line there.
```
prompt> cloc
Usage: cloc [options] <file(s)/dir(s)> | <set 1> <set 2> | <report files>
Input Options :
               --diff <set1> <set2>
               --csv  :  Write the results as comma separated values.
               --out=<file>  :  Synonym for --report-file=<file>.
```
#### Team Member Details
```
1. Harsh Mehta : harshmehta493@gmail.com
2. Yash Chandreshkumar Golwala : golwalayash@gmail.com
3. Raghav Dutta : raghav.dutta29@gmail.com
4. Navroop Virk : virknavroop@gmail.com
5. Manisha Jalota : manisha.jalota223@gmail.com
```

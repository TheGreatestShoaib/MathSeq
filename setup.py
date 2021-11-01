from setuptools import setup, find_packages
long_description = open('README.md',"r").read()

setup(

    name ='mathseq',
    version ='0.0.1',
    description ='A sample Python project',
    long_description = long_description,
    long_description_content_type ='text/markdown',
    url ='https://github.com/TheGreatestShoaib/Mathseq',
    author ='Shoaib Islam',
    author_email ='shoaibislam.sh@gmail.com',
    classifiers =[

        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Build Tools :: Reseach',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='sequence, generator, fibonacci',
    packages=['mathseq'],
    python_requires ='>=3.6, <4',
    project_urls={ 
        'Bug Reports': 'https://github.com/TheGreatestShoaib/MathSeq/issues',
        'Source': 'https://github.com/TheGreatestShoaib/MathSeq/',
    },
    
    )

long_description.close()
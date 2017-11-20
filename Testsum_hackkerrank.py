{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fnil\fcharset0 Menlo-Italic;\f1\fnil\fcharset0 Menlo-Bold;\f2\fnil\fcharset0 Menlo-Regular;
}
{\colortbl;\red255\green255\blue255;\red109\green109\blue109;\red0\green0\blue109;\red14\green110\blue109;
\red0\green0\blue254;}
{\*\expandedcolortbl;;\csgenericrgb\c42745\c42745\c42745;\csgenericrgb\c0\c0\c42745;\csgenericrgb\c5490\c43137\c42745;
\csgenericrgb\c0\c0\c99608;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh15300\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\i\fs24 \cf2 #!/bin/python3\
\

\f1\i0\b \cf3 import 
\f2\b0 \cf0 sys\
\
arr = \cf3 list\cf0 (\cf3 map\cf0 (\cf3 int\cf0 , \cf3 input\cf0 ().strip().split(
\f1\b \cf4 ' '
\f2\b0 \cf0 )))\
\
max_val = \cf3 max\cf0 (arr)\
min_val = \cf3 min\cf0 (arr)\
\

\f1\b \cf3 if 
\f2\b0 int\cf0 (max_val) == \cf3 int\cf0 (min_val):\
    total_max = \cf3 sum\cf0 (arr)\
    total_min = \cf3 sum\cf0 (arr)\

\f1\b \cf3 else
\f2\b0 \cf0 :\
    total_max = \cf3 int\cf0 (\cf5 0\cf0 )\
    total_min = \cf3 int\cf0 (\cf5 0\cf0 )\
    i = \cf3 int\cf0 (\cf5 0\cf0 )\
    j = \cf3 int\cf0 (\cf5 0\cf0 )\
\
    length = \cf3 int\cf0 (\cf3 len\cf0 (arr))\
\
    
\f1\b \cf3 for 
\f2\b0 \cf0 i 
\f1\b \cf3 in 
\f2\b0 range\cf0 (length):\
        total_max += (\cf3 int\cf0 (arr[i]) 
\f1\b \cf3 if 
\f2\b0 int\cf0 (arr[i]) != \cf3 int\cf0 (min_val) 
\f1\b \cf3 else 
\f2\b0 \cf5 0\cf0 )\
\
    
\f1\b \cf3 for 
\f2\b0 \cf0 j 
\f1\b \cf3 in 
\f2\b0 range\cf0 (length):\
        total_min += (\cf3 int\cf0 (arr[j]) 
\f1\b \cf3 if 
\f2\b0 int\cf0 (arr[j]) != \cf3 int\cf0 (max_val) 
\f1\b \cf3 else 
\f2\b0 \cf5 0\cf0 )\
\
\cf3 print\cf0 (total_min, total_max)\
}
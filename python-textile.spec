%include	/usr/lib/rpm/macros.python

%define         module textile

Summary:	Humane Web Text Generator
Summary(pl):	Konwerter czystego tekstu do HTML
Name:		python-%{module}
Version:	1.13
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://dealmeida.net/code/%{module}-%{version}.tgz
# Source0-md5:	08ba85593d36346b64120227d2e3d9c4
URL:		http://www.diveintomark.org/projects/pytextile/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyTextile is a Python port of Textile, Dean Allen's Humane Web Text
Generator. It's main purpose is to convert plain text to HTML using
popular markup (ie. _something_ means underline, *something* means
emphasis etc.)

%description -l pl
PyTextile jest przepisan± do Pythona wersj± programu Textile. S³u¿y on
do konwersji czystego tekstu do formatu HTML, wykorzystuj±c do tego
popularne znaczniki (np. _co¶_ oznacza podkre¶lenie, *co¶*
wyt³uszczenie itp.)

%prep
%setup -q -n %{module}

%build
python -c "import compiler;compiler.compileFile('textile.py')"
python -c "import compileall; compileall.compile_dir('yaml')"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}{,/yaml}
install %{module}.pyc $RPM_BUILD_ROOT%{py_sitedir}
install yaml/*.py[co] $RPM_BUILD_ROOT%{py_sitedir}/yaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py[co]
%dir %{py_sitedir}/yaml
%{py_sitedir}/yaml/*.py[co]


%define		module	textile

Summary:	Humane Web Text Generator
Summary(pl):	Konwerter czystego tekstu do HTML
Name:		python-%{module}
Version:	2.0.10
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://dealmeida.net/code/%{module}-%{version}.tar.gz
# Source0-md5:	19ae07379e5986049b7d9a34ffcbf867
URL:		http://www.diveintomark.org/projects/pytextile/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
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
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]

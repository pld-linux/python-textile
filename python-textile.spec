
%define		module	textile

Summary:	Humane Web Text Generator
Summary(pl.UTF-8):	Konwerter czystego tekstu do HTML
Name:		python-%{module}
Version:	2.1.5
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/t/textile/%{module}-%{version}.tar.gz
# Source0-md5:	6e030e112eca1dafa1be84cf5575560d
URL:		http://pypi.python.org/pypi/textile
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyTextile is a Python port of Textile, Dean Allen's Humane Web Text
Generator. It's main purpose is to convert plain text to HTML using
popular markup (ie. _something_ means underline, *something* means
emphasis etc.)

%description -l pl.UTF-8
PyTextile jest przepisaną do Pythona wersją programu Textile. Służy on
do konwersji czystego tekstu do formatu HTML, wykorzystując do tego
popularne znaczniki (np. _coś_ oznacza podkreślenie, *coś*
wytłuszczenie itp.)

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
